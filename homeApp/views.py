from django.shortcuts import render
from django.views.generic import TemplateView
from siteSettingsApp.models import settingModel, footerLinkBox, Slider
from productionsApp.models import CategoryParent


class indexView(TemplateView):
    template_name = 'homeApp/index.html'
    model = CategoryParent

    def get_context_data(self, **kwargs):
        categoriesParents = CategoryParent.objects.filter(isActive=True)[:6]
        settings = settingModel.objects.filter(isMainSettings=True).first()
        sliders = Slider.objects.filter(isActive=True)
        context = {
            'sliders': sliders,
            'categoriesParents': categoriesParents,
            'settings': settings,
        }
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
