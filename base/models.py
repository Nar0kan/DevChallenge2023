from django.db import models


class Sheet(models.Model):
    """Class represents a sheet"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Cell(models.Model):
    """Class represents a single cell in a sheet"""
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    cell_key = models.CharField(max_length=8, unique=True, primary_key=True)
    
    value = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.cell_key}: {self.value}"
