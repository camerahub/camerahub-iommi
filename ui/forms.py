from iommi import Form
from schema.models import Battery, CameraModel, Manufacturer, Mount, PaperStock, Accessory, Archive, EnlargerModel, Developer, Format, FlashModel, FilmStock, LensModel, Process, Filter, Flash, Teleconverter, TeleconverterModel
from schema.models import Enlarger, BulkFilm, Camera, Lens, MountAdapter, NegativeSize

def battery_edit(request, slug):
    return Form.edit(
        auto__instance=Battery.objects.get(slug=slug),
    )

def cameramodel_edit(request, slug):
    return Form.edit(
        auto__instance=CameraModel.objects.get(slug=slug),
    )

def manufacturer_create(request, slug):
    return Form.create(
        auto__model=Manufacturer
    )

def manufacturer_edit(request, slug):
    return Form.edit(
        auto__instance=Manufacturer.objects.get(slug=slug),
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

def format_edit(request, slug):
    return Form.edit(
        auto__instance=Format.objects.get(slug=slug),
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

def process_edit(request, slug):
    return Form.edit(
        auto__instance=Process.objects.get(slug=slug),
    )

def filter_edit(request, slug):
    return Form.edit(
        auto__instance=Filter.objects.get(slug=slug),
    )

def flash_edit(request, slug):
    return Form.edit(
        auto__instance=Flash.objects.get(slug=slug),
    )

def teleconvertermodel_edit(request, slug):
    return Form.edit(
        auto__instance=TeleconverterModel.objects.get(slug=slug),
    )

def teleconverter_edit(request, slug):
    return Form.edit(
        auto__instance=Teleconverter.objects.get(slug=slug),
    )

def enlarger_edit(request, slug):
    return Form.edit(
        auto__instance=Enlarger.objects.get(slug=slug),
    )

def bulkfilm_edit(request, slug):
    return Form.edit(
        auto__instance=BulkFilm.objects.get(slug=slug),
    )

def camera_edit(request, slug):
    return Form.edit(
        auto__instance=Camera.objects.get(slug=slug),
    )

def lens_edit(request, slug):
    return Form.edit(
        auto__instance=Lens.objects.get(slug=slug),
    )

def mountadapter_edit(request, slug):
    return Form.edit(
        auto__instance=MountAdapter.objects.get(slug=slug),
    )

def negativesize_edit(request, slug):
    return Form.edit(
        auto__instance=NegativeSize.objects.get(slug=slug),
    )
