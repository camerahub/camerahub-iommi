from django.shortcuts import get_object_or_404
from django.template import Template, loader
from iommi import Page, html
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, EnlargerModel, Enlarger

class IndexPage(Page):
    title = html.h1('Placeholder')

def accessory_view(request, id_owner):
    obj = get_object_or_404(Accessory, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/accessory_detail.html")
    class AccessoryPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return AccessoryPage(context=context)

def archive_view(request, id_owner):
    obj = get_object_or_404(Archive, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/archive_detail.html")
    class ArchivePage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return ArchivePage(context=context)

def battery_view(request, slug):
    obj = get_object_or_404(Battery, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/battery_detail.html")
    class BatteryPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return BatteryPage(context=context)

def bulkfilm_view(request, slug):
    obj = get_object_or_404(BulkFilm, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/bulkfilm_detail.html")
    class BulkFilmPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return BulkFilmPage(context=context)

def camera_view(request, id_owner):
    obj = get_object_or_404(Camera, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/camera_detail.html")
    class CameraPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return CameraPage(context=context)

def cameramodel_view(request, slug):
    obj = get_object_or_404(CameraModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/cameramodel_detail.html")
    class CameraModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return CameraModelPage(context=context)

def developer_view(request, slug):
    obj = get_object_or_404(Developer, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/developer_detail.html")
    class DeveloperPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return DeveloperPage(context=context)

def enlargermodel_view(request, slug):
    obj = get_object_or_404(EnlargerModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/developer_detail.html")
    class EnlargerModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return EnlargerModelPage(context=context)

def manufacturer_view(request, slug):
    obj = get_object_or_404(Manufacturer, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/manufacturer_detail.html")
    class ManufacturerPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return ManufacturerPage(context=context)
