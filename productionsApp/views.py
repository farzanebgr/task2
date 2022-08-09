from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Products, ProductsCategory, CategoryParent, ProductsBrand, ProductsComments
from django.views.generic import ListView, DetailView


class ProductionsDetailView(DetailView):
    model = Products
    template_name = 'productionsApp/detailsProductions.html'

    def get_queryset(self):
        query = super(ProductionsDetailView, self).get_queryset()
        query = query.filter(isActive=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ProductionsDetailView, self).get_context_data()
        product: Products = kwargs.get('object')
        context['comments'] = ProductsComments.objects.filter(product_id=product.id, parent=None).order_by(
            '-createDate').prefetch_related('productscomments_set')
        context['comments_count'] = ProductsComments.objects.filter(product_id=product.id).count()
        return context


def addProductComment(request: HttpRequest):
    if request.user.is_authenticated:
        product_comment = request.GET.get('product_comment')
        product_id = request.GET.get('product_id')
        parent_id = request.GET.get('parent_id')
        print(product_id, product_comment, parent_id)
        new_comment = ProductsComments(product_id=product_id, message=product_comment, user_id=request.user.id,
                                       parent_id=parent_id)
        new_comment.save()

        context = {
            'comments': ProductsComments.objects.filter(product_id=product_id, parent_id=None).order_by(
                '-createDate').prefetch_related('productscomments_set'),
            'commentCount': ProductsComments.objects.filter(product_id=product_id).count()
        }
        return render(request, 'productionsApp/includes/commentsProduction.html', context)

    return HttpResponse('response')


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


class BrandsListView(ListView):
    template_name = 'productionsApp/brandsList.html'
    model = ProductsBrand
    context_object_name = 'brands'
    paginate_by = 2

    def get_queryset(self):
        base_query = super(BrandsListView, self).get_queryset()
        allBrands = base_query.filter(isActive=True)
        return allBrands


class BrandDetailView(DetailView):
    model = ProductsBrand
    template_name = 'productionsApp/brandDetail.html'


def categories_productions_partial(request: HttpResponse):
    productions_main_categories = CategoryParent.objects.filter(isActive=True)
    context = {
        'main_categories': productions_main_categories
    }
    return render(request, 'productionsApp/includes/categoryPartial.html', context)
