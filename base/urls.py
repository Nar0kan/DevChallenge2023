from django.urls import path
from .views import *

app_name = "base"

urlpatterns = [
    path('api/v1/<str:sheet_id>/<str:cell_id>/', updateCellValue, name='update-cell-value'),
    path('api/v1/<str:sheet_id>/', getAllCells, name='get-all-cells'),
]
