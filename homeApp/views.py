from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from siteSettingsApp.models import settingModel, footerLinkBox, Slider
from productionsApp.models import Products
from utils.convertors import group_list


class indexView(TemplateView):
    template_name = 'homeApp/index.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(isActive=True)
        context['sliders'] = sliders
        latest_products = Products.objects.filter(isActive=True, isDelete=False).order_by('-id')[:12]
        most_visit_products = Products.objects.filter(isActive=True, isDelete=False).annotate(
            visit_count=Count('productsvisit')).order_by('-productsvisit')[:12]

        context['latest_products'] = group_list(latest_products)
        context['most_visit_products'] = group_list(most_visit_products)
        return context


class aboutUsView(TemplateView):
    template_name = 'homeApp/aboutUs.html'

    def get_context_data(self, **kwargs):
        context = super(aboutUsView, self).get_context_data()
        siteSettongs: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettongs'] = siteSettongs
        return context


def siteHeaderPartial(request):
    settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    context = {
        'settings': settings
    }
    return render(request, 'shared/header.html', context)


def siteFooterPartial(request):
    settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    footer_link_boxes = footerLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set

    context = {
        'settings': settings,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/footer.html', context)
