from iommi import Form, Table
from django.urls import path
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from iommi import register_factory
from iommi.path import register_path_decoding

from taggit.managers import TaggableManager

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

from .pages import manufacturer_view
from .tables import manufacturer_table

# Workaround for https://github.com/iommirocks/iommi/issues/339
register_factory(GenericRelation, factory=None)
register_factory(GenericForeignKey, factory=None)
register_factory(TaggableManager, shortcut_name='many_to_many')

register_path_decoding(
    manufacturer_name=Manufacturer.name,
    manufacturer_pk=Manufacturer,
)

urlpatterns = [
    # ...your urls...
    path('', Table(auto__model=Manufacturer).as_view(), name='index'),
    path('manufacturer/', manufacturer_table, name='manufacturer-list'),
    path('manufacturer/create', Form.create(auto__model=Manufacturer).as_view(), name='manufacturer-create'),
    path('manufacturer/<slug>/', manufacturer_view)
]
