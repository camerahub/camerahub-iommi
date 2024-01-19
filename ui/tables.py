from django.urls import reverse_lazy
from iommi import Table, Action, Column
from schema.models import Manufacturer, CameraModel

class ManufacturerTable(Table):
    select = Column.select()  # Shortcut for creating checkboxes to select rows

    class Meta:
        auto__model=Manufacturer
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('manufacturer-create'))

class CameraModelTable(Table):

    class Meta:
        auto__model=CameraModel
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('cameramodel-create'))
