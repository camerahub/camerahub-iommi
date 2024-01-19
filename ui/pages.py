from django.shortcuts import get_object_or_404
from django.template import Template, loader
from iommi import Page, html
from schema.models import Manufacturer

class IndexPage(Page):
    title = html.h1('Placeholder')

def manufacturer_view(request, slug):
    obj = get_object_or_404(Manufacturer, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/manufacturer_detail.html")

    class ManufacturerPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    
    return ManufacturerPage(context=context)
