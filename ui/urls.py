from iommi import Form, Table
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from iommi import register_factory
from iommi.path import register_path_decoding

from taggit.managers import TaggableManager

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, EnlargerModel, Enlarger
from schema.models import FilmStock, Filter, Flash, FlashModel, Format, Lens, LensModel, Manufacturer, Mount, MountAdapter, NegativeSize
from schema.models import PaperStock, Person, Print, Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

from .tables import AccessoryTable, ArchiveTable, BatteryTable, BulkFilmTable, CameraTable, CameraModelTable, DeveloperTable, EnlargerModelTable
from .tables import EnlargerTable, FilmStockTable, FilterTable, FlashTable, FlashModelTable, FormatTable, LensTable, LensModelTable
from .tables import ManufacturerTable, MountTable, MountAdapterTable, NegativeSizeTable, PaperStockTable, PersonTable, PrintTable, ProcessTable
from .tables import ScanTable, NegativeTable, FilmTable, TagTable, TeleconverterTable, TeleconverterModelTable, TonerTable

from .pages import accessory_view, archive_view, battery_view, bulkfilm_view, camera_view, cameramodel_view, developer_view
from .pages import enlargermodel_view, enlarger_view, film_view, filmstock_view, filter_view, flash_view, flashmodel_view, format_view
from .pages import lens_view, lensmodel_view, manufacturer_view, mount_view, mountadapter_view, negative_view, negativesize_view, paperstock_view
from .pages import person_view, print_view, process_view, scan_view, teleconverter_view, teleconvertermodel_view, toner_view, IndexPage

from .forms import battery_edit, cameramodel_edit, manufacturer_edit, manufacturer_create, mount_edit, paperstock_edit, accessory_edit, archive_edit, enlargermodel_edit, developer_edit, format_edit, flashmodel_edit, filmstock_edit, lensmodel_edit, process_edit, filter_edit, flash_edit, teleconverter_edit, teleconvertermodel_edit

# Workaround for https://github.com/iommirocks/iommi/issues/339
register_factory(GenericRelation, factory=None)
register_factory(GenericForeignKey, factory=None)
register_factory(TaggableManager, shortcut_name='many_to_many')

register_path_decoding(
    manufacturer_name=Manufacturer.name,
    manufacturer_pk=Manufacturer,
)

urlpatterns = [
    # Static pages
    path('', IndexPage().as_view(), name='index'),
    path('stats', IndexPage().as_view(), name='stats'),
    path('mystats', IndexPage().as_view(), name='mystats'),
    path('search/', IndexPage().as_view(), name='search'),

    path('tag/', TagTable().as_view(), name='tag-list'),
#    path('tag/<slug:slug>', views.TagDetail.as_view(), name='tag-detail'),
#    path('tag-autocomplete/', views.TagAutocomplete.as_view(), name='tag-autocomplete'),

    path('accessory/', AccessoryTable().as_view(), name='accessory-list'),
    path('accessory/<id_owner>', accessory_view, name='accessory-detail'),
    path('accessory/create', Form.create(auto__model=Accessory).as_view(), name='accessory-create'),
    path('accessory/<int:id_owner>/edit', accessory_edit, name='accessory-update'),

    path('archive/', ArchiveTable().as_view(), name='archive-list'),
    path('archive/<id_owner>', archive_view, name='archive-detail'),
    path('archive/create', Form.create(auto__model=Archive).as_view(), name='archive-create'),
#    path('archive/<int:id_owner>/print', views.ArchivePrint.as_view(), name='archive-print'),
    path('archive/<int:id_owner>/edit', archive_edit, name='archive-update'),

    path('battery/', BatteryTable().as_view(), name='battery-list'),
    path('battery/<slug>', battery_view, name='battery-detail'),
    path('battery/create', Form.create(auto__model=Battery).as_view(), name='battery-create'),
    path('battery/<slug:slug>/edit', battery_edit, name='battery-update'),

    path('bulkfilm/', BulkFilmTable().as_view(), name='bulkfilm-list'),
    path('bulkfilm/<slug>', bulkfilm_view, name='bulkfilm-detail'),
    path('bulkfilm/create', Form.create(auto__model=BulkFilm).as_view(), name='bulkfilm-create'),
    path('bulkfilm/<int:id_owner>/edit', bulkfilm_edit, name='bulkfilm-update'),

    path('camera/', CameraTable().as_view(), name='camera-list'),
    path('camera/<id_owner>', camera_view, name='camera-detail'),
    path('camera/create', Form.create(auto__model=Camera).as_view(), name='camera-create'),
    path('camera/<int:id_owner>/edit', camera_edit, name='camera-update'),
#    path('camera/<int:id_owner>/sell', views.CameraSell.as_view(), name='camera-sell'),

    path('cameramodel/', CameraModelTable().as_view(), name='cameramodel-list'), 
    path('cameramodel/<slug>', cameramodel_view, name='cameramodel-detail'),
    path('cameramodel/create', Form.create(auto__model=CameraModel).as_view(), name='cameramodel-create'),
    path('cameramodel/<slug:slug>/edit', cameramodel_edit, name='cameramodel-update'),

    path('developer/', DeveloperTable().as_view(), name='developer-list'),
    path('developer/<slug>', developer_view, name='developer-detail'),
    path('developer/create', Form.create(auto__model=Developer).as_view(), name='developer-create'),
    path('developer/<slug:slug>/edit', developer_edit, name='developer-update'),

    path('enlargermodel/', EnlargerModelTable().as_view(), name='enlargermodel-list'),
    path('enlargermodel/<slug>', enlargermodel_view, name='enlargermodel-detail'),
    path('enlargermodel/create', Form.create(auto__model=EnlargerModel).as_view(), name='enlargermodel-create'),
    path('enlargermodel/<slug:slug>/edit', enlargermodel_edit, name='enlargermodel-update'),

    path('enlarger/', EnlargerTable().as_view(), name='enlarger-list'),
    path('enlarger/<id_owner>', enlarger_view, name='enlarger-detail'),
    path('enlarger/create', Form.create(auto__model=Enlarger).as_view(), name='enlarger-create'),
    path('enlarger/<int:id_owner>/edit', enlarger_edit, name='enlarger-update'),

    path('filmstock/', FilmStockTable().as_view(), name='filmstock-list'),
    path('filmstock/<slug>', filmstock_view, name='filmstock-detail'),
    path('filmstock/create', Form.create(auto__model=FilmStock).as_view(), name='filmstock-create'),
    path('filmstock/<slug:slug>/edit', filmstock_edit, name='filmstock-update'),

    path('filter/', FilterTable().as_view(), name='filter-list'),
    path('filter/<pk>', filter_view, name='filter-detail'),
    path('filter/create', Form.create(auto__model=Filter).as_view(), name='filter-create'),
    path('filter/<int:pk>/edit', filter_edit, name='filter-update'),

    path('flash/', FlashTable().as_view(), name='flash-list'),
    path('flash/<id_owner>', flash_view, name='flash-detail'),
    path('flash/create', Form.create(auto__model=Flash).as_view(), name='flash-create'),
    path('flash/<int:id_owner>/edit', flash_edit, name='flash-update'),

    path('flashmodel/', FlashModelTable().as_view(), name='flashmodel-list'),
    path('flashmodel/<slug>', flashmodel_view, name='flashmodel-detail'),
    path('flashmodel/create', Form.create(auto__model=FlashModel).as_view(), name='flashmodel-create'),
    path('flashmodel/<slug:slug>/edit', flashmodel_edit, name='flashmodel-update'),

    path('format/', FormatTable().as_view(), name='format-list'),
    path('format/<pk>', format_view, name='flashmodel-detail'),
    path('format/create', Form.create(auto__model=Format).as_view(), name='format-create'),
    path('format/<int:pk>/edit', format_edit, name='format-update'),

    path('lens/', LensTable().as_view(), name='lens-list'),
    path('lens/<id_owner>', lens_view, name='lens-detail'),
    path('lens/create', Form.create(auto__model=Lens).as_view(), name='lens-create'),
    path('lens/<int:id_owner>/edit', lens_edit, name='lens-update'),
#    path('lens/<int:id_owner>/sell', views.LensSell.as_view(), name='lens-sell'),

    path('lensmodel/', LensModelTable().as_view(), name='lensmodel-list'),
    path('lensmodel/<slug>', lensmodel_view, name='lensmodel-detail'),
    path('lensmodel/create', Form.create(auto__model=LensModel).as_view(), name='lensmodel-create'),
    path('lensmodel/<slug:slug>/edit', lensmodel_edit, name='lensmodel-update'),

    path('manufacturer/', ManufacturerTable().as_view(), name='manufacturer-list'),    
    path('manufacturer/create', ManufacturerForm.create().as_view(), name='manufacturer-create'),
    path('manufacturer/<slug>', manufacturer_view, name='manufacturer-detail'),         
    #path('manufacturer/<slug:slug>/update', views.ManufacturerUpdate.as_view(), name='manufacturer-update'),

    path('mount/', MountTable().as_view(), name='mount-list'),
    path('mount/<slug>', mount_view, name='mount-detail'),         
    path('mount/create/', Form.create(auto__model=Mount).as_view(), name='mount-create'),
    path('mount/<slug:slug>/edit', mount_edit, name='mount-update'),

    path('mountadapter/', MountAdapterTable().as_view(), name='mountadapter-list'),
    path('mountadapter/<id_owner>', mountadapter_view, name='mountadapter-detail'),
    path('mountadapter/create/', Form.create(auto__model=MountAdapter).as_view(), name='mountadapter-create'),
    path('mountadapter/<int:id_owner>/edit', mountadapter_edit, name='mountadapter-update'),

    path('negativesize/', NegativeSizeTable().as_view(), name='negativesize-list'),
    path('negativesize/<pk>', negativesize_view, name='negativesize-detail'),
    path('negativesize/create/', Form.create(auto__model=NegativeSize).as_view(), name='negativesize-create'),
    path('negativesize/<int:pk>/edit', negativesize_edit, name='negativesize-update'),

    path('paperstock/', PaperStockTable().as_view(), name='paperstock-list'),
    path('paperstock/<pk>', paperstock_view, name='paperstock-detail'),
    path('paperstock/create', Form.create(auto__model=PaperStock).as_view(), name='paperstock-create'),
    path('paperstock/<int:pk>/edit', paperstock_edit, name='paperstock-update'),

    path('person/', PersonTable().as_view(), name='person-list'),
    path('person/<id_owner>', person_view, name='person-detail'),
    path('person/create', Form.create(auto__model=Person).as_view(), name='person-create'),
#    path('person/<int:id_owner>/update', views.PersonUpdate.as_view(), name='person-update'),

    path('print/', PrintTable().as_view(), name='print-list'),
    path('print/<id_owner>', print_view, name='print-detail'),
#    path('print/<int:id_owner>/print', views.PrintPrint.as_view(), name='print-print'),
    path('print/create', Form.create(auto__model=Print).as_view(), name='print-create'),
#    path('print/<int:id_owner>/update', views.PrintUpdate.as_view(), name='print-update'),
#    path('print/<int:id_owner>/archive', views.PrintArchive.as_view(), name='print-archive'),
#    path('print/<int:id_owner>/sell', views.PrintSell.as_view(), name='print-sell'),

    path('process/', ProcessTable().as_view(), name='process-list'),
    path('process/<id_owner>', process_view, name='process-detail'),
    path('process/create', Form.create(auto__model=Process).as_view(), name='process-create'),
    path('process/<int:pk>/edit', process_edit, name='process-update'),

    path('scan/', ScanTable().as_view(), name='scan-list'),
    path('scan/<uuid>', scan_view, name='scan-detail'),
    path('scan/create', Form.create(auto__model=Scan).as_view(), name='scan-create'),
#    path('scan/<uuid:uuid>/update', views.ScanUpdate.as_view(), name='scan-update'),

    path('negative/', NegativeTable().as_view(), name='negative-list'),
    path('negative/<slug>', negative_view, name='negative-detail'),
    path('negative/create', Form.create(auto__model=Negative).as_view(), name='negative-create'),
#    path('negative/<str:slug>/update', views.NegativeUpdate.as_view(), name='negative-update'),

    path('film/', FilmTable().as_view(), name='film-list'),
    path('film/<id_owner>', film_view, name='film-detail'),
    path('film/create', Form.create(auto__model=Film).as_view(), name='film-create'),
#    path('film/<int:id_owner>/update', views.FilmUpdate.as_view(), name='film-update'),
#    path('film/<int:id_owner>/print', views.FilmPrint.as_view(), name='film-print'),
#    path('film/<int:id_owner>/load', views.FilmLoad.as_view(), name='film-load'),
#    path('film/<int:id_owner>/develop', views.FilmDevelop.as_view(), name='film-develop'),
#    path('film/<int:id_owner>/archive', views.FilmArchive.as_view(), name='film-archive'),

    path('teleconverter/', TeleconverterTable().as_view(), name='teleconverter-list'),
    path('teleconverter/<id_owner>', teleconverter_view, name='teleconverter-detail'),
    path('teleconverter/create', Form.create(auto__model=Teleconverter).as_view(), name='teleconverter-create'),
    path('teleconverter/<int:id_owner>/edit', teleconverter_edit, name='teleconverter-update'),

    path('teleconvertermodel/', TeleconverterModelTable().as_view(), name='teleconvertermodel-list'),
    path('teleconvertermodel/<slug>', teleconvertermodel_view, name='teleconvertermodel-detail'),
    path('teleconvertermodel/create', Form.create(auto__model=TeleconverterModel).as_view(), name='teleconvertermodel-create'),
    path('teleconvertermodel/<slug:slug>/edit', teleconvertermodel_edit, name='teleconvertermodel-update'),

    path('toner/', TonerTable().as_view(), name='toner-list'),
    path('toner/<slug>', toner_view, name='toner-detail'),
    path('toner/create', Form.create(auto__model=Toner).as_view(), name='toner-create'),
#    path('toner/<slug:slug>/update', views.TonerUpdate.as_view(), name='toner-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
