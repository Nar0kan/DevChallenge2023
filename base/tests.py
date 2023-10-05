#from django.test import TestCase
#import requests

from .models import *

from django.test import TestCase, Client
import json

class YourAPITestCase(TestCase):
    def setUp(self):
        # Initialize the Django test client
        self.client = Client()

        sheet = Sheet.objects.create(title='devchallenge-test')
        cell_1 = Cell.objects.create(sheet=sheet, cell_key='var0', value='20', result='20')
        cell_2 = Cell.objects.create(sheet=sheet, cell_key='var2', value='113', result='113')


    # Positive Test Cases
    def test_get_all_cells_positive(self):
        response = self.client.get('/api/v1/devchallenge-test/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

    def test_update_cell_value_positive(self):
        data = {"value": "5"}
        data_json = json.dumps(data)
        response = self.client.post(
            '/api/v1/devchallenge-test/var1/',
            data_json,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        
        # Optionally, you can parse the JSON response content if needed
        response_data = json.loads(response.content.decode('utf-8'))
    def test_get_cell_value_positive(self):
        response = self.client.get('/api/v1/devchallenge-test/var2/')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_update_cell_value_with_formula_positive(self):
        data = {"value": "=var1+var2"}
        data_json = json.dumps(data)
        response = self.client.post('/api/v1/devchallenge-test/var3/', data_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    # Negative Test Cases
    def test_get_all_cells_with_invalid_sheet_id(self):
        response = self.client.get('/api/v1/nonexistent-sheet/')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.content.decode('utf-8'))

    def test_update_cell_value_with_invalid_sheet_id(self):
        data = {"value": "5"}
        response = self.client.post('/api/v1/nonexistent-sheet/v0r109/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.content.decode('utf-8'))

    def test_get_cell_value_with_invalid_sheet_id(self):
        response = self.client.get('/api/v1/nonexistent-sheet/v0r109/')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.content.decode('utf-8'))

    def test_update_cell_value_with_invalid_json(self):
        data = "invalid json"
        response = self.client.post('/api/v1/devchallenge-test/var1/', data, content_type='application/json')
        self.assertEqual(response.status_code, 422)
        data = json.loads(response.content.decode('utf-8'))

    def test_update_cell_value_with_invalid_formula(self):
        data = {"value": "=var2+var99"}  # Reference to a non-existent cell
        response = self.client.post('/api/v1/devchallenge-test/var4/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 422)
        data = json.loads(response.content.decode('utf-8'))

# class YourAPITestCase(TestCase):

#     def setUp(self):
#         # Set up any test data or configurations needed
#         try:
#             sheet = Sheet.objects.create(title='devchallenge-xx')
#         except Exception as e:
#             pass

#         cell_1 = Cell.objects.create(Sheet=sheet, cell_key='var1', value='20', result='20')
#         cell_2 = Cell.objects.create(Sheet=sheet, cell_key='var1', value='113', result='113')


#     def testGetCellValue(self):
#         response = requests.get('http://localhost:8000/api/v1/devchallenge-xx/var1')
#         self.assertEqual(response.status_code, 201)

#         data = response.json()

#         self.assertEqual(data['value'], '20')
#         self.assertEqual(data['result'], '20')


#     def testGetCellValueError(self):
#         response = requests.get('http://localhost:8000/api/v1/devchallenge-xx/var3')
#         self.assertEqual(response.status_code, 404)


#     def testNewCellValue(self):
#         response = requests.post('http://localhost:8000/api/v1/devchallenge-xx/var3')
#         self.assertEqual(response.status_code, 201)

#         data = response.json()

#         self.assertEqual(data['value'], '10')
#         self.assertEqual(data['result'], '15')

#     def test_get_all_cells(self):
#         # Make a GET request to your API endpoint for fetching all cells
#         response = requests.get('http://localhost:8000/api/v1/devchallenge-xx')

#         # Assert the response status code
#         self.assertEqual(response.status_code, 200)

#         # Parse the JSON response
#         data = response.json()

#         # Assert the expected structure of the response, e.g., check if 'cells' key is present
#         self.assertIn('cells', data)

#         # Assert the expected number of cells or specific cell data
#         self.assertEqual(len(data['cells']), 3)
#         self.assertEqual(data['cells'][0]['cell_key'], 'var1')
#         # Add more assertions as needed