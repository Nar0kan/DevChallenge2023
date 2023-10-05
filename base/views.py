from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
import re

from .models import *


@api_view(['GET'])
def getAllCells(request, sheet_id):
    try:
        sheet_obj = Sheet.objects.get(title=sheet_id)
        cells = Cell.objects.filter(sheet=sheet_obj)
        cell_data = {}

        for cell in cells:
            cell_data[cell.cell_key] = {'value': cell.value, 'result': cell.result}

        return JsonResponse(cell_data, status=200)
    except Exception as e:
        return JsonResponse({'error': 'ERROR'}, status=404)


@api_view(['POST', 'GET'])
def updateCellValue(request, sheet_id, cell_id):
    cell_value = None

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            cell_value = data.get('value')

            try:
                sheet_obj = Sheet.objects.get(title=sheet_id)
            except Exception as e:
                return JsonResponse({'error': f'Sheet "{sheet_id}" does not exist.'}, status=404)

            try:
                cell_obj = Cell.objects.get(sheet=sheet_obj, cell_key=cell_id)
            except Exception as e:
                cell_obj =  Cell.objects.create(sheet=sheet_obj, cell_key=cell_id)

            if cell_value.startswith('='):
                formula = cell_value[1:]
                cell_refs = re.findall(r'var\d+', formula)

                for cell_ref in cell_refs:
                    try:
                        ref_cell_obj = Cell.objects.get(sheet=sheet_obj, cell_key=cell_ref)
                        formula = formula.replace(cell_ref, str(ref_cell_obj.value))
                    except Cell.DoesNotExist:
                        return JsonResponse({'value': f'{cell_value}', 'result': 'ERROR'}, status=422)

                try:
                    result = eval(formula)

                    cell_obj.value = str(result)
                    cell_obj.save()

                    response_data = {
                        'value': f'{cell_value}',
                        'result': str(result),
                    }
                    return JsonResponse(response_data, status=201)
                except Exception as e:
                    return JsonResponse({'value': f'{cell_value}', 'result': 'ERROR'}, status=422)

            cell_obj.value = cell_value
            cell_obj.save()

            response_data = {
                'value': f'{cell_value}',
                'result': f'{cell_value}',
            }
            return JsonResponse(response_data, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'value': f'{cell_value}', 'result': 'ERROR'}, status=422)

    if request.method == 'GET':
        try:
            sheet_obj = Sheet.objects.get(title=sheet_id)
            cell_obj = Cell.objects.get(sheet=sheet_obj, cell_key=cell_id)

            response_data = {
                'value': cell_obj.value,
                'result': cell_obj.result,
            }

            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({'error': 'ERROR'}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
