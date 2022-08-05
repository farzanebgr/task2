from django.http import HttpResponse
from django.shortcuts import render

from .models import Products, ProductsCategory, CategoryParent
from django.views.generic import ListView, DetailView


class DetailsProductionsView(DetailView):
    template_name = 'productionsApp/detailsProductions.html'
    model = Products


class CategoriesProductionsView(ListView):
    template_name = 'productionsApp/categoriesProductions.html'
    model = ProductsCategory
    context_object_name = 'categories'
    ordering = ['title']
    paginate_by = 8

    def get_queryset(self):
        base_query = super(CategoriesProductionsView, self).get_queryset()
        categoryProduction = base_query.filter(isActive=True)
        return categoryProduction


class AllProductionsView(ListView):
    template_name = 'productionsApp/allProductions.html'
    model = Products
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 8

    def get_queryset(self):
        base_query = super(AllProductionsView, self).get_queryset()
        allProductions = base_query.filter(isActive=True)
        return allProductions


def categories_productions_partial(request: HttpResponse):
    productions_main_categories = CategoryParent.objects.filter(isActive=True)
    context = {
        'main_categories': productions_main_categories
    }
    return render(request, 'productionsApp/includes/categoryPartial.html', context)
