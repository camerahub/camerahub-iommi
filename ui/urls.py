from iommi import Form, Table
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from iommi import register_factory
from iommi.path import register_path_decoding

from taggit.managers import TaggableManager

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, EnlargerModel, Enlarger
from schema.models import FilmStock, Filter, Flash, FlashModel, Format, Lens, LensModel, Manufacturer, PaperStock
from schema.models import Person, Print, Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

from .tables import AccessoryTable, ArchiveTable, BatteryTable, BulkFilmTable, CameraTable, CameraModelTable, DeveloperTable, EnlargerModelTable
from .tables import EnlargerTable, FilmStockTable, FilterTable, FlashTable, FlashModelTable, FormatTable, LensTable, LensModelTable
from .tables import ManufacturerTable, MountTable, MountAdapterTable, NegativeSizeTable, PaperStockTable, PersonTable, PrintTable, ProcessTable
from .tables import ScanTable, NegativeTable, FilmTable, TagTable, TeleconverterTable, TeleconverterModelTable, TonerTable

from .pages import manufacturer_view, IndexPage

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
#    path('accessory/<int:id_owner>', views.AccessoryDetail.as_view(), name='accessory-detail'),
    path('accessory/create', Form.create(auto__model=Accessory).as_view(), name='accessory-create'),
#    path('accessory/<int:id_owner>/update', views.AccessoryUpdate.as_view(), name='accessory-update'),

    path('archive/', ArchiveTable().as_view(), name='archive-list'),
#    path('archive/<int:id_owner>', views.ArchiveDetail.as_view(), name='archive-detail'),
    path('archive/create', Form.create(auto__model=Archive).as_view(), name='archive-create'),
#    path('archive/<int:id_owner>/print', views.ArchivePrint.as_view(), name='archive-print'),
#    path('archive/<int:id_owner>/update', views.ArchiveUpdate.as_view(), name='archive-update'),

    path('battery/', BatteryTable().as_view(), name='battery-list'),
#    path('battery/<slug:slug>', views.BatteryDetail.as_view(), name='battery-detail'),
    path('battery/create', Form.create(auto__model=Battery).as_view(), name='battery-create'),
#    path('battery/<slug:slug>/update', views.BatteryUpdate.as_view(), name='battery-update'),

    path('bulkfilm/', BulkFilmTable().as_view(), name='bulkfilm-list'),
#    path('bulkfilm/<int:id_owner>', views.BulkFilmDetail.as_view(), name='bulkfilm-detail'),
    path('bulkfilm/create', Form.create(auto__model=BulkFilm).as_view(), name='bulkfilm-create'),
#    path('bulkfilm/<int:id_owner>/update', views.BulkFilmUpdate.as_view(), name='bulkfilm-update'),

    path('camera/', CameraTable().as_view(), name='camera-list'),
#    path('camera/<int:id_owner>', views.CameraDetail.as_view(), name='camera-detail'),
    path('camera/create', Form.create(auto__model=Camera).as_view(), name='camera-create'),
#    path('camera/<int:id_owner>/update', views.CameraUpdate.as_view(), name='camera-update'),
#    path('camera/<int:id_owner>/sell', views.CameraSell.as_view(), name='camera-sell'),

    path('cameramodel/', CameraModelTable().as_view(), name='cameramodel-list'), 
#    path('cameramodel/<slug:slug>', views.CameraModelDetail.as_view(), name='cameramodel-detail'),
    path('cameramodel/create', Form.create(auto__model=CameraModel).as_view(), name='cameramodel-create'),
#    path('cameramodel/<slug:slug>/update', views.CameraModelUpdate.as_view(), name='cameramodel-update'),

    path('developer/', DeveloperTable().as_view(), name='developer-list'),
#    path('developer/<slug:slug>', views.DeveloperDetail.as_view(), name='developer-detail'),
    path('developer/create', Form.create(auto__model=Developer).as_view(), name='developer-create'),
#    path('developer/<slug:slug>/update', views.DeveloperUpdate.as_view(), name='developer-update'),

    path('enlargermodel/', EnlargerModelTable().as_view(), name='enlargermodel-list'),
#    path('enlargermodel/<slug:slug>', views.EnlargerModelDetail.as_view(), name='enlargermodel-detail'),
    path('enlargermodel/create', Form.create(auto__model=EnlargerModel).as_view(), name='enlargermodel-create'),
#    path('enlargermodel/<slug:slug>/update', views.EnlargerModelUpdate.as_view(), name='enlargermodel-update'),

    path('enlarger/', EnlargerTable().as_view(), name='enlarger-list'),
#    path('enlarger/<int:id_owner>', views.EnlargerDetail.as_view(), name='enlarger-detail'),
    path('enlarger/create', Form.create(auto__model=Enlarger).as_view(), name='enlarger-create'),
#    path('enlarger/<int:id_owner>/update', views.EnlargerUpdate.as_view(), name='enlarger-update'),

    path('filmstock/', FilmStockTable().as_view(), name='filmstock-list'),
#    path('filmstock/<slug:slug>', views.FilmStockDetail.as_view(), name='filmstock-detail'),
    path('filmstock/create', Form.create(auto__model=FilmStock).as_view(), name='filmstock-create'),
#    path('filmstock/<slug:slug>/update', views.FilmStockUpdate.as_view(), name='filmstock-update'),

    path('filter/', FilterTable().as_view(), name='filter-list'),
#    path('filter/<int:pk>', views.FilterDetail.as_view(), name='filter-detail'),
    path('filter/create', Form.create(auto__model=Filter).as_view(), name='filter-create'),
#    path('filter/<int:pk>/update', views.FilterUpdate.as_view(), name='filter-update'),

    path('flash/', FlashTable().as_view(), name='flash-list'),
#    path('flash/<int:id_owner>', views.FlashDetail.as_view(), name='flash-detail'),
    path('flash/create', Form.create(auto__model=Flash).as_view(), name='flash-create'),
#    path('flash/<int:id_owner>/update', views.FlashUpdate.as_view(), name='flash-update'),

    path('flashmodel/', FlashModelTable().as_view(), name='flashmodel-list'),
#    path('flashmodel/<slug:slug>', views.FlashModelDetail.as_view(), name='flashmodel-detail'),
    path('flashmodel/create', Form.create(auto__model=FlashModel).as_view(), name='flashmodel-create'),
#    path('flashmodel/<slug:slug>/update', views.FlashModelUpdate.as_view(), name='flashmodel-update'),

    path('format/', FormatTable().as_view(), name='format-list'),
#    path('format/<int:pk>', views.FormatDetail.as_view(), name='format-detail'),
    path('format/create', Form.create(auto__model=Format).as_view(), name='format-create'),
#    path('format/<int:pk>/update', views.FormatUpdate.as_view(), name='format-update'),

    path('lens/', LensTable().as_view(), name='lens-list'),
#    path('lens/<int:id_owner>', views.LensDetail.as_view(), name='lens-detail'),
    path('lens/create', Form.create(auto__model=Lens).as_view(), name='lens-create'),
#    path('lens/<int:id_owner>/update', views.LensUpdate.as_view(), name='lens-update'),
#    path('lens/<int:id_owner>/sell', views.LensSell.as_view(), name='lens-sell'),

    path('lensmodel/', LensModelTable().as_view(), name='lensmodel-list'),
#    path('lensmodel/<slug:slug>', views.LensModelDetail.as_view(), name='lensmodel-detail'),
    path('lensmodel/create', Form.create(auto__model=LensModel).as_view(), name='lensmodel-create'),
#    path('lensmodel/<slug:slug>/update', views.LensModelUpdate.as_view(), name='lensmodel-update'),

    path('manufacturer/', ManufacturerTable().as_view(), name='manufacturer-list'),    
    path('manufacturer/create', Form.create(auto__model=Manufacturer).as_view(), name='manufacturer-create'),
    path('manufacturer/<slug>/', manufacturer_view, name='manufacturer-detail'),         
    #path('manufacturer/<slug:slug>/update', views.ManufacturerUpdate.as_view(), name='manufacturer-update'),

    path('mount/', MountTable().as_view(), name='mount-list'),
    #path('mount/<slug:slug>', views.MountDetail.as_view(), name='mount-detail'),
    #path('mount/create/', views.MountCreate.as_view(), name='mount-create'),
    #path('mount/<slug:slug>/update', views.MountUpdate.as_view(), name='mount-update'),

    path('mountadapter/', MountAdapterTable().as_view(), name='mountadapter-list'),
    #path('mountadapter/<int:id_owner>', views.MountAdapterDetail.as_view(), name='mountadapter-detail'),
    #path('mountadapter/create/', views.MountAdapterCreate.as_view(), name='mountadapter-create'),
    #path('mountadapter/<int:id_owner>/update', views.MountAdapterUpdate.as_view(), name='mountadapter-update'),

    path('negativesize/', NegativeSizeTable().as_view(), name='negativesize-list'),
    #path('negativesize/<int:pk>', views.NegativeSizeDetail.as_view(), name='negativesize-detail'),
    #path('negativesize/create/', views.NegativeSizeCreate.as_view(), name='negativesize-create'),
    #path('negativesize/<int:pk>/update', views.NegativeSizeUpdate.as_view(), name='negativesize-update'),

    path('paperstock/', PaperStockTable().as_view(), name='paperstock-list'),
#    path('paperstock/<int:pk>', views.PaperStockDetail.as_view(), name='paperstock-detail'),
    path('paperstock/create', Form.create(auto__model=PaperStock).as_view(), name='paperstock-create'),
#    path('paperstock/<int:pk>/update', views.PaperStockUpdate.as_view(), name='paperstock-update'),

    path('person/', PersonTable().as_view(), name='person-list'),
#    path('person/<int:id_owner>', views.PersonDetail.as_view(), name='person-detail'),
    path('person/create', Form.create(auto__model=Person).as_view(), name='person-create'),
#    path('person/<int:id_owner>/update', views.PersonUpdate.as_view(), name='person-update'),

    path('print/', PrintTable().as_view(), name='print-list'),
#    path('print/<int:id_owner>', views.PrintDetail.as_view(), name='print-detail'),
#    path('print/<int:id_owner>/print', views.PrintPrint.as_view(), name='print-print'),
    path('print/create', Form.create(auto__model=Print).as_view(), name='print-create'),
#    path('print/<int:id_owner>/update', views.PrintUpdate.as_view(), name='print-update'),
#    path('print/<int:id_owner>/archive', views.PrintArchive.as_view(), name='print-archive'),
#    path('print/<int:id_owner>/sell', views.PrintSell.as_view(), name='print-sell'),

    path('process/', ProcessTable().as_view(), name='process-list'),
#    path('process/<int:pk>', views.ProcessDetail.as_view(), name='process-detail'),
    path('process/create', Form.create(auto__model=Process).as_view(), name='process-create'),
#    path('process/<int:pk>/update', views.ProcessUpdate.as_view(), name='process-update'),

    path('scan/', ScanTable().as_view(), name='scan-list'),
#    path('scan/<uuid:uuid>', views.ScanDetail.as_view(), name='scan-detail'),
    path('scan/create', Form.create(auto__model=Scan).as_view(), name='scan-create'),
#    path('scan/<uuid:uuid>/update', views.ScanUpdate.as_view(), name='scan-update'),

    path('negative/', NegativeTable().as_view(), name='negative-list'),
#    path('negative/<str:slug>', views.NegativeDetail.as_view(), name='negative-detail'),
    path('negative/create', Form.create(auto__model=Negative).as_view(), name='negative-create'),
#    path('negative/<str:slug>/update', views.NegativeUpdate.as_view(), name='negative-update'),

    path('film/', FilmTable().as_view(), name='film-list'),
#    path('film/<int:id_owner>', views.FilmDetail.as_view(), name='film-detail'),
    path('film/create', Form.create(auto__model=Film).as_view(), name='film-create'),
#    path('film/<int:id_owner>/update', views.FilmUpdate.as_view(), name='film-update'),
#    path('film/<int:id_owner>/print', views.FilmPrint.as_view(), name='film-print'),
#    path('film/<int:id_owner>/load', views.FilmLoad.as_view(), name='film-load'),
#    path('film/<int:id_owner>/develop', views.FilmDevelop.as_view(), name='film-develop'),
#    path('film/<int:id_owner>/archive', views.FilmArchive.as_view(), name='film-archive'),

    path('teleconverter/', TeleconverterTable().as_view(), name='teleconverter-list'),
#    path('teleconverter/<int:id_owner>', views.TeleconverterDetail.as_view(), name='teleconverter-detail'),
    path('teleconverter/create', Form.create(auto__model=Teleconverter).as_view(), name='teleconverter-create'),
#    path('teleconverter/<int:id_owner>/update', views.TeleconverterUpdate.as_view(), name='teleconverter-update'),

    path('teleconvertermodel/', TeleconverterModelTable().as_view(), name='teleconvertermodel-list'),
#    path('teleconvertermodel/<slug:slug>', views.TeleconverterModelDetail.as_view(), name='teleconvertermodel-detail'),
    path('teleconvertermodel/create', Form.create(auto__model=TeleconverterModel).as_view(), name='teleconvertermodel-create'),
#    path('teleconvertermodel/<slug:slug>/update', views.TeleconverterModelUpdate.as_view(), name='teleconvertermodel-update'),

    path('toner/', TonerTable().as_view(), name='toner-list'),
#    path('toner/<slug:slug>', views.TonerDetail.as_view(), name='toner-detail'),
    path('toner/create', Form.create(auto__model=Toner).as_view(), name='toner-create'),
#    path('toner/<slug:slug>/update', views.TonerUpdate.as_view(), name='toner-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
