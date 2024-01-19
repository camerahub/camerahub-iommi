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

#class CameraModelTable(Table):
#    class Meta:
#        auto__model=CameraModel
#        query_from_indexes=True
#        actions__add=Action(attrs__href=reverse_lazy('cameramodel-create'))

class AccessoryTable(Table):
    id_owner = Column()
    model = Column()
    type = Column()
    class Meta:
        auto__model = Accessory

class ArchiveTable(Table):
    class Meta:  
        auto__model = Archive
        #fields = ('name', 'type', 'max_size', 'sealed')


class BatteryTable(Table):
    class Meta:
        auto__model = Battery
        #fields = ('name', 'voltage', 'chemistry')


class BulkFilmTable(Table):
    class Meta:
        auto__model = BulkFilm
        #fields = ('id_owner', 'format', 'filmstock', 'length', 'finished')


class CameraTable(Table):
    class Meta:
        auto__model = Camera
        #fields = ('id_owner', 'cameramodel', 'serial', 'manufactured', 'cameramodel__mount', 'cameramodel__lens_model_name', 'own')


class CameraModelTable(Table):
    model = Column()
    mount = Column()
    lens_model_name = Column()
    format = Column()
    introduced = Column()
    body_type = Column()
    negative_size = Column()

    class Meta:
        auto__model=CameraModel
        # Disable some columns
        columns__disambiguation__include = False
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('cameramodel-create'))


class DeveloperTable(Table):
    class Meta:
        auto__model = Developer
        #fields = ('name', 'for_paper', 'for_film')


class EnlargerModelTable(Table):
    class Meta:
        auto__model = EnlargerModel
        #fields = ('model', 'negative_size', 'type')


class EnlargerTable(Table):
    class Meta:
        auto__model = Enlarger
        #fields = ('id_owner', 'enlargermodel')


class FilmStockTable(Table):
    class Meta:
        auto__model = FilmStock
        #fields = ('name', 'iso', 'colour', 'panchromatic', 'process')


class FilterTable(Table):
    class Meta:
        auto__model = Filter
        #fields = ('type', 'shortname', 'attenuation')


class FlashModelTable(Table):
    class Meta:
        auto__model = FlashModel
        #fields = ('model', 'guide_number', 'ttl')


class FlashTable(Table):
    class Meta:
        auto__model = Flash
        #fields = ('id_owner', 'flashmodel')


class FormatTable(Table):
    class Meta:
        auto__model = Format
        #fields = ('format',)


class LensTable(Table):
    class Meta:
        auto__model = Lens
        #fields = ('id_owner', 'lensmodel', 'lensmodel__mount', 'serial', 'manufactured', 'own')


class LensModelTable(Table):
    class Meta:
        auto__model = LensModel
        #fields = ('model', 'mount', 'zoom', 'focal_length', 'max_aperture', 'autofocus', 'introduced')


class ManufacturerTable(Table):
    select = Column.select()  # Shortcut for creating checkboxes to select rows

    class Meta:
        auto__model=Manufacturer
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('manufacturer-create'))


class MountTable(Table):
    class Meta:
        auto__model = Mount
        #fields = ('mount', 'shutter_in_lens', 'type', 'purpose')


class MountAdapterTable(Table):
    class Meta:
        auto__model = MountAdapter
        #fields = ('id_owner', 'camera_mount', 'lens_mount', 'has_optics', 'infinity_focus')


class NegativeSizeTable(Table):
    class Meta:
        auto__model = NegativeSize
        #fields = ('name', 'size', 'crop_factor', 'area', 'aspect_ratio')


class PaperStockTable(Table):
    class Meta:
        auto__model = PaperStock
        #fields = ('name', 'resin_coated', 'colour', 'finish')


class PersonTable(Table):
    class Meta:
        auto__model = Person
        #fields = ('id_owner', 'name', 'type')


class PrintTable(Table):
    class Meta:
        auto__model = Print
        #fields = ('id_owner', 'negative', 'date', 'size', 'own', 'archive')


class ProcessTable(Table):
    class Meta:
        auto__model = Process
        #fields = ('name', 'colour', 'positive')


class ScanTable(Table):
    class Meta:
        auto__model = Scan
        #fields = ('uuid', 'negative', 'print', 'filename', 'date')


class NegativeTable(Table):
    class Meta:
        auto__model = Negative
        #fields = ('slug', 'film', 'date', 'film__camera', 'lens', 'shutter_speed', 'aperture')


class FilmTable(Table):
    class Meta:
        auto__model = Film
        #fields = ('id_owner', 'filmstock', 'format', 'status', 'negative_set__count', 'date_processed', 'camera')


class TagTable(Table):
    class Meta:
        auto__model = Tag
        #fields = ('id_owner', 'teleconvertermodel',)


class TeleconverterTable(Table):
    class Meta:
        auto__model = Teleconverter
        #fields = ('id_owner', 'teleconvertermodel',)


class TeleconverterModelTable(Table):
    class Meta:
        auto__model = TeleconverterModel
        #fields = ('model', 'mount', 'factor')


class TonerTable(Table):
    class Meta:        
        auto__model = Toner
        #fields = ('name', 'formulation', 'stock_dilution')
