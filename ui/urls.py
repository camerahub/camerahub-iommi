from iommi import Form, Table, Action, html
from django.urls import path
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from iommi import register_factory
from iommi.path import register_path_decoding

from taggit.managers import TaggableManager

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

# Workaround for https://github.com/iommirocks/iommi/issues/339
register_factory(GenericRelation, factory=None)
register_factory(GenericForeignKey, factory=None)
register_factory(TaggableManager, shortcut_name='many_to_many')

urlpatterns = [
    # ...your urls...
    path('', Table(auto__model=Manufacturer).as_view(), name='index'),
    path('manufacturer/', Table(auto__model=Manufacturer, container__children__bar=html.div('Bar', after=0), query_from_indexes=True, actions__add=Action(attrs__href='/'), ).as_view(), name='manufacturer-list'),
    path('manufacturer/create', Form.create(auto__model=Manufacturer).as_view(), name='manufacturer-create'),
]
