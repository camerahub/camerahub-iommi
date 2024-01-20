# pylint: disable=no-member
from django.urls import reverse_lazy
from iommi import Table, Action, Column
#from django.utils.html import format_html
#from schema.funcs import boolicon, colouricon

# Import all models that need tables
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner
from taggit.models import Tag

class AccessoryTable(Table):
    class Meta:
        auto__model = Accessory
        auto__include=['id_owner', 'model', 'type']

class ArchiveTable(Table):
    class Meta:  
        auto__model = Archive
        auto__include= ('name', 'type', 'max_size', 'sealed')


class BatteryTable(Table):
    class Meta:
        auto__model = Battery
        auto__include= ('name', 'voltage', 'chemistry')


class BulkFilmTable(Table):
    class Meta:
        auto__model = BulkFilm
        auto__include= ('id_owner', 'format', 'filmstock', 'length', 'finished')


class CameraTable(Table):
    class Meta:
        auto__model = Camera
        auto__include= ('id_owner', 'cameramodel', 'serial', 'manufactured', 'cameramodel__mount', 'cameramodel__lens_model_name', 'own')


class CameraModelTable(Table):
    class Meta:
        auto__model=CameraModel
        auto__include=('manufacturer', 'model', 'mount', 'lens_model_name', 'format', 'introduced', 'body_type', 'negative_size')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('cameramodel-create'))


class DeveloperTable(Table):
    class Meta:
        auto__model = Developer
        auto__include= ('name', 'for_paper', 'for_film')


class EnlargerModelTable(Table):
    class Meta:
        auto__model = EnlargerModel
        auto__include= ('model', 'negative_size', 'type')


class EnlargerTable(Table):
    class Meta:
        auto__model = Enlarger
        auto__include= ('id_owner', 'enlargermodel')


class FilmStockTable(Table):
    class Meta:
        auto__model = FilmStock
        auto__include= ('name', 'iso', 'colour', 'panchromatic', 'process')


class FilterTable(Table):
    class Meta:
        auto__model = Filter
        auto__include= ('type', 'shortname', 'attenuation')


class FlashModelTable(Table):
    class Meta:
        auto__model = FlashModel
        auto__include= ('model', 'guide_number', 'ttl')


class FlashTable(Table):
    class Meta:
        auto__model = Flash
        auto__include= ('id_owner', 'flashmodel')


class FormatTable(Table):
    class Meta:
        auto__model = Format
        auto__include= ('format',)


class LensTable(Table):
    class Meta:
        auto__model = Lens
        auto__include= ('id_owner', 'lensmodel', 'lensmodel__mount', 'serial', 'manufactured', 'own')


class LensModelTable(Table):
    class Meta:
        auto__model = LensModel
        auto__include= ('model', 'mount', 'zoom', 'focal_length', 'max_aperture', 'autofocus', 'introduced')


class ManufacturerTable(Table):
    select = Column.select()  # Shortcut for creating checkboxes to select rows

    class Meta:
        auto__model=Manufacturer
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('manufacturer-create'))


class MountTable(Table):
    class Meta:
        auto__model = Mount
        auto__include= ('mount', 'shutter_in_lens', 'type', 'purpose')


class MountAdapterTable(Table):
    class Meta:
        auto__model = MountAdapter
        auto__include= ('id_owner', 'camera_mount', 'lens_mount', 'has_optics', 'infinity_focus')


class NegativeSizeTable(Table):
    class Meta:
        auto__model = NegativeSize
        auto__include= ('name', 'size', 'crop_factor', 'area', 'aspect_ratio')


class PaperStockTable(Table):
    class Meta:
        auto__model = PaperStock
        auto__include= ('name', 'resin_coated', 'colour', 'finish')


class PersonTable(Table):
    class Meta:
        auto__model = Person
        auto__include= ('id_owner', 'name', 'type')


class PrintTable(Table):
    class Meta:
        auto__model = Print
        auto__include= ('id_owner', 'negative', 'date', 'size', 'own', 'archive')


class ProcessTable(Table):
    class Meta:
        auto__model = Process
        auto__include= ('name', 'colour', 'positive')


class ScanTable(Table):
    class Meta:
        auto__model = Scan
        auto__include= ('uuid', 'negative', 'print', 'filename', 'date')


class NegativeTable(Table):
    class Meta:
        auto__model = Negative
        auto__include= ('slug', 'film', 'date', 'film__camera', 'lens', 'shutter_speed', 'aperture')


class FilmTable(Table):
    class Meta:
        auto__model = Film
        auto__include= ('id_owner', 'filmstock', 'format', 'status', 'negative_set__count', 'date_processed', 'camera')


class TagTable(Table):
    class Meta:
        auto__model = Tag
        auto__include= ('id_owner', 'teleconvertermodel',)


class TeleconverterTable(Table):
    class Meta:
        auto__model = Teleconverter
        auto__include= ('id_owner', 'teleconvertermodel',)


class TeleconverterModelTable(Table):
    class Meta:
        auto__model = TeleconverterModel
        auto__include= ('model', 'mount', 'factor')


class TonerTable(Table):
    class Meta:        
        auto__model = Toner
        auto__include= ('name', 'formulation', 'stock_dilution')
