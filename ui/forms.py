from django.http import HttpResponseRedirect
from iommi import Form
from schema.models import Manufacturer

class ManufacturerForm(Form):
    class Meta:
        auto__model=Manufacturer
