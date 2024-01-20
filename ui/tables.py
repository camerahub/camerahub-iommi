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
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('accessory-create'))

class ArchiveTable(Table):
    class Meta:  
        auto__model = Archive
        auto__include= ('name', 'type', 'max_size', 'sealed')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('archive-create'))


class BatteryTable(Table):
    class Meta:
        auto__model = Battery
        auto__include= ('name', 'voltage', 'chemistry')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('battery-create'))


class BulkFilmTable(Table):
    class Meta:
        auto__model = BulkFilm
        auto__include= ('id_owner', 'format', 'filmstock', 'length', 'finished')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('bulkfilm-create'))


class CameraTable(Table):
    class Meta:
        auto__model = Camera
        auto__include= ('id_owner', 'cameramodel', 'serial', 'manufactured', 'cameramodel__mount', 'cameramodel__lens_model_name', 'own')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('camera-create'))


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
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('developer-create'))


class EnlargerModelTable(Table):
    class Meta:
        auto__model = EnlargerModel
        auto__include= ('model', 'negative_size', 'type')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('enlargermodel-create'))


class EnlargerTable(Table):
    class Meta:
        auto__model = Enlarger
        auto__include= ('id_owner', 'enlargermodel')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('enlarger-create'))


class FilmStockTable(Table):
    class Meta:
        auto__model = FilmStock
        auto__include= ('name', 'iso', 'colour', 'panchromatic', 'process')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('filmstock-create'))


class FilterTable(Table):
    class Meta:
        auto__model = Filter
        auto__include= ('type', 'shortname', 'attenuation')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('filter-create'))


class FlashModelTable(Table):
    class Meta:
        auto__model = FlashModel
        auto__include= ('model', 'guide_number', 'ttl')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('flashmodel-create'))


class FlashTable(Table):
    class Meta:
        auto__model = Flash
        auto__include= ('id_owner', 'flashmodel')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('flash-create'))


class FormatTable(Table):
    class Meta:
        auto__model = Format
        auto__include= ('format',)
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('format-create'))


class LensTable(Table):
    class Meta:
        auto__model = Lens
        auto__include= ('id_owner', 'lensmodel', 'lensmodel__mount', 'serial', 'manufactured', 'own')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('lens-create'))


class LensModelTable(Table):
    class Meta:
        auto__model = LensModel
        auto__include= ('model', 'mount', 'zoom', 'focal_length', 'max_aperture', 'autofocus', 'introduced')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('lensmodel-create'))


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
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('mount-create'))


class MountAdapterTable(Table):
    class Meta:
        auto__model = MountAdapter
        auto__include= ('id_owner', 'camera_mount', 'lens_mount', 'has_optics', 'infinity_focus')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('mountadapter-create'))


class NegativeSizeTable(Table):
    class Meta:
        auto__model = NegativeSize
        auto__include= ('name', 'size', 'crop_factor', 'area', 'aspect_ratio')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('negativesize-create'))


class PaperStockTable(Table):
    class Meta:
        auto__model = PaperStock
        auto__include= ('name', 'resin_coated', 'colour', 'finish')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('paperstock-create'))


class PersonTable(Table):
    class Meta:
        auto__model = Person
        auto__include= ('id_owner', 'name', 'type')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('person-create'))


class PrintTable(Table):
    class Meta:
        auto__model = Print
        auto__include= ('id_owner', 'negative', 'date', 'size', 'own', 'archive')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('print-create'))


class ProcessTable(Table):
    class Meta:
        auto__model = Process
        auto__include= ('name', 'colour', 'positive')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('process-create'))


class ScanTable(Table):
    class Meta:
        auto__model = Scan
        auto__include= ('uuid', 'negative', 'print', 'filename', 'date')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('scan-create'))


class NegativeTable(Table):
    class Meta:
        auto__model = Negative
        auto__include= ('slug', 'film', 'date', 'film__camera', 'lens', 'shutter_speed', 'aperture')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('negative-create'))


class FilmTable(Table):
    class Meta:
        auto__model = Film
        auto__include= ('id_owner', 'filmstock', 'format', 'status', 'negative_set__count', 'date_processed', 'camera')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('film-create'))


class TagTable(Table):
    class Meta:
        auto__model = Tag
        query_from_indexes=True
        #actions__add=Action(attrs__href=reverse_lazy('tag-create'))


class TeleconverterTable(Table):
    class Meta:
        auto__model = Teleconverter
        auto__include= ('id_owner', 'teleconvertermodel',)
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('teleconverter-create'))


class TeleconverterModelTable(Table):
    class Meta:
        auto__model = TeleconverterModel
        auto__include= ('model', 'mount', 'factor')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('teleconvertermodel-create'))


class TonerTable(Table):
    class Meta:        
        auto__model = Toner
        auto__include= ('name', 'formulation', 'stock_dilution')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('toner-create'))
