from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from siteSettingsApp.models import settingModel, footerLinkBox, Slider
from productionsApp.models import Products
from utils.convertors import group_list


# Show Sliders, The Latest products, site setting model
class indexView(TemplateView):
    template_name = 'homeApp/index.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get site setting model
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings

        # Get Sliders
        sliders = Slider.objects.filter(isActive=True)
        context['sliders'] = sliders

        # Get The Latest products
        latest_products = Products.objects.filter(isActive=True, isDelete=False).order_by('-id')[:12]
        context['latest_products'] = group_list(latest_products)

        return context

# Show a particular setting model in about us
class aboutUsView(TemplateView):
    template_name = 'homeApp/aboutUs.html'

    def get_context_data(self, **kwargs):
        context = super(aboutUsView, self).get_context_data()

        # Get site setting model
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings

        return context


# Show a particular setting model
def siteHeaderPartial(request):
    settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    context = {
        'settings': settings
    }
    return render(request, 'shared/header.html', context)


# Show a particular setting model, footer link boxes
def siteFooterPartial(request):
    siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    footer_link_boxes = footerLinkBox.objects.all()

    for item in footer_link_boxes:
        item.footerlink_set

    context = {
        'siteSettings': siteSettings,
        'footer_link_boxes': footer_link_boxes
    }

    return render(request, 'shared/footer.html', context)
