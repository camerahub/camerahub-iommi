from django.urls import reverse_lazy
from iommi import Table, Action, html, Column
from schema.models import Manufacturer

def manufacturer_table(request):

    class ManufacturerTable(Table):
        select = Column.select()  # Shortcut for creating checkboxes to select rows

    return ManufacturerTable(auto__model=Manufacturer, container__children__bar=html.div('Bar', after=0), query_from_indexes=True, actions__add=Action(attrs__href=reverse_lazy('manufacturer-create')))
