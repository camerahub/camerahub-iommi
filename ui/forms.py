from iommi import Form
from schema.models import Battery, CameraModel, Manufacturer, Mount, PaperStock, Accessory, Archive, EnlargerModel, Developer, Format, FlashModel, FilmStock, LensModel, Process, Filter, Flash, Teleconverter, TeleconverterModel
from schema.models import Enlarger, BulkFilm, Camera, Lens, MountAdapter, NegativeSize, Person, Scan, Negative, Film, Print, Toner

def battery_edit(request, slug):
    return Form.edit(
        auto__instance=Battery.objects.get(slug=slug),
    )

def cameramodel_edit(request, slug):
    return Form.edit(
        auto__instance=CameraModel.objects.get(slug=slug),
    )

def manufacturer_create(request, manufacturer_slug):
    return Form.create(
        auto__model=Manufacturer
    )

def manufacturer_edit(request, manufacturer_slug):
    return Form.edit(
        auto__instance=Manufacturer.objects.get(slug=manufacturer_slug),
    )

def mount_edit(request, slug):
    return Form.edit(
        auto__instance=Mount.objects.get(slug=slug),
    )

def paperstock_edit(request, pk):
    return Form.edit(
        auto__instance=PaperStock.objects.get(pk=pk),
    )

def accessory_edit(request, id_owner):
    return Form.edit(
        auto__instance=Accessory.objects.get(id_owner=id_owner),
    )

def archive_edit(request, id_owner):
    return Form.edit(
        auto__instance=Archive.objects.get(id_owner=id_owner),
    )

def enlargermodel_edit(request, id_owner):
    return Form.edit(
        auto__instance=EnlargerModel.objects.get(id_owner=id_owner),
    )

def developer_edit(request, slug):
    return Form.edit(
        auto__instance=Developer.objects.get(slug=slug),
    )

def format_edit(request, pk):
    return Form.edit(
        auto__instance=Format.objects.get(pk=pk),
    )

def flashmodel_edit(request, slug):
    return Form.edit(
        auto__instance=FlashModel.objects.get(slug=slug),
    )

def filmstock_edit(request, slug):
    return Form.edit(
        auto__instance=FilmStock.objects.get(slug=slug),
    )

def lensmodel_edit(request, slug):
    return Form.edit(
        auto__instance=LensModel.objects.get(slug=slug),
    )

def process_edit(request, pk):
    return Form.edit(
        auto__instance=Process.objects.get(pk=pk),
    )

def filter_edit(request, pk):
    return Form.edit(
        auto__instance=Filter.objects.get(pk=pk),
    )

def flash_edit(request, id_owner):
    return Form.edit(
        auto__instance=Flash.objects.get(id_owner=id_owner),
    )

def teleconvertermodel_edit(request, slug):
    return Form.edit(
        auto__instance=TeleconverterModel.objects.get(slug=slug),
    )

def teleconverter_edit(request, id_owner):
    return Form.edit(
        auto__instance=Teleconverter.objects.get(id_owner=id_owner),
    )

def enlarger_edit(request, id_owner):
    return Form.edit(
        auto__instance=Enlarger.objects.get(id_owner=id_owner),
    )

def bulkfilm_edit(request, id_owner):
    return Form.edit(
        auto__instance=BulkFilm.objects.get(id_owner=id_owner),
    )

def camera_edit(request, id_owner):
    return Form.edit(
        auto__instance=Camera.objects.get(id_owner=id_owner),
    )

def lens_edit(request, id_owner):
    return Form.edit(
        auto__instance=Lens.objects.get(id_owner=id_owner),
    )

def mountadapter_edit(request, id_owner):
    return Form.edit(
        auto__instance=MountAdapter.objects.get(id_owner=id_owner),
    )

def negativesize_edit(request, pk):
    return Form.edit(
        auto__instance=NegativeSize.objects.get(pk=pk),
    )

def person_edit(request, id_owner):
    return Form.edit(
        auto__instance=Person.objects.get(id_owner=id_owner),
    )

def scan_edit(request, uuid):
    return Form.edit(
        auto__instance=Scan.objects.get(uuid=uuid),
    )

def negative_edit(request, slug):
    return Form.edit(
        auto__instance=Negative.objects.get(slug=slug),
    )

def film_edit(request, id_owner):
    return Form.edit(
        auto__instance=Film.objects.get(id_owner=id_owner),
    )

def print_edit(request, id_owner):
    return Form.edit(
        auto__instance=Print.objects.get(id_owner=id_owner),
    )

def toner_edit(request, slug):
    return Form.edit(
        auto__instance=Toner.objects.get(slug=slug),
    )
