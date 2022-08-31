from django.db.models import Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from siteSettingsApp.models import settingModel
from utils.httpService import get_client_ip
from productionsApp.models import Products, ProductsCategory, CategoryParent, ProductsBrand, ProductsComments, \
    BrandsComments, ProductsVisit, ProductGallery
from django.views.generic import ListView, DetailView
from utils.convertors import group_list


# Show each Product Detail in single page
class ProductionsDetailView(DetailView):
    model = Products
    template_name = 'productionsApp/detailsProductions.html'

    # Get Particular Product from database
    def get_queryset(self):
        query = super(ProductionsDetailView, self).get_queryset()
        query = query.filter(isActive=True)
        return query

    # Get site setting model, visit count, galleries pictures, check visit product and show comments if have permission
    def get_context_data(self, **kwargs):
        context = super(ProductionsDetailView, self).get_context_data()

        loaded_product = self.object
        product: Products = kwargs.get('object')

        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings

        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['product_galleries'] = group_list(galleries, 3)

        user_ip = get_client_ip(self.request)
        user_id = None

        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductsVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductsVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.pk)
            new_visit.save()

        context['visit'] = ProductsVisit.objects.filter(product_id=product.id).count()

        if Products.haveComments:
            context['comments'] = ProductsComments.objects.filter(product_id=product.id, parent=None) \
                .order_by('-createDate').prefetch_related('productscomments_set')
            context['comments_count'] = ProductsComments.objects.filter(product_id=product.id).count()
            return context


# Add Product comment if user login into site
def addProductComment(request: HttpRequest):
    if request.user.is_authenticated:
        product_comment = request.GET.get('product_comment')
        product_id = request.GET.get('product_id')
        parent_id = request.GET.get('parent_id')

        new_comment = ProductsComments(product_id=product_id, message=product_comment,
                                       user_id=request.user.id, parent_id=parent_id)
        new_comment.save()

        context = {
            'comments': ProductsComments.objects.filter(product_id=product_id, parent_id=None) \
                .order_by('-createDate').prefetch_related('productscomments_set'),
            'commentCount': ProductsComments.objects.filter(product_id=product_id).count()
        }

        return render(request, 'productionsApp/includes/commentsProduction.html', context)


# Group by categories in the Side menu
class CategoriesProductionsView(ListView):
    model = ProductsCategory
    context_object_name = 'categories'

    # Get all categories from database
    def get_queryset(self):
        base_query = super(CategoriesProductionsView, self).get_queryset()
        categoryProduction = base_query.filter(isActive=True)
        return categoryProduction

    # Show site settings model in page
    def get_context_data(self, **kwargs):
        context = super(CategoriesProductionsView, self).get_context_data()
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings
        return context


# Show all Products by pagination 6
class AllProductionsView(ListView):
    template_name = 'productionsApp/allProductions.html'
    model = Products
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 6

    # Get Product details from database
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllProductionsView, self).get_context_data()

        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()

        query = Products.objects.all()

        product: Products = query.order_by('-price').first()

        db_max_price = product.price if product is not None else 0

        # To filter price
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price

        context['siteSettings'] = siteSettings

        return context

    # Get all details
    def get_queryset(self):
        query = super(AllProductionsView, self).get_queryset()

        brand_name = self.kwargs.get('brand')
        category_name = self.kwargs.get('cat')

        request: HttpRequest = self.request

        # To filter price

        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        # To filter categories
        if category_name is not None:
            query = query.filter(category__urlTitle__iexact=category_name)

        if brand_name is not None:
            query = query.filter(brand__titleEN__iexact=brand_name)

        return query


# Show all Products by pagination 2
class BrandsListView(ListView):
    template_name = 'productionsApp/brandsList.html'
    model = ProductsBrand
    context_object_name = 'brands'
    paginate_by = 2

    # Get Brand detail from database
    def get_queryset(self):
        base_query = super(BrandsListView, self).get_queryset()
        allBrands = base_query.filter(isActive=True)
        return allBrands

    # Show site settings model in page
    def get_context_data(self, **kwargs):
        context = super(BrandsListView, self).get_context_data()
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings
        return context


# Show Brand details from database
class BrandDetailView(DetailView):
    model = ProductsBrand
    template_name = 'productionsApp/brandDetail.html'

    # Get brand detail
    def get_queryset(self):
        query = super(BrandDetailView, self).get_queryset()
        query = query.filter(isActive=True)
        return query

    # Get site setting model, and show brand comment if it has permission
    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data()

        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings

        # Show brand comment
        if ProductsBrand.haveComments:
            brand: ProductsBrand = kwargs.get('object')
            context['comments'] = BrandsComments.objects.filter(brand_id=brand.id, parent_id=None) \
                .order_by('-createDate').prefetch_related('brandscomments_set')
            context['comments_count'] = BrandsComments.objects.filter(isActive=True).count()

            return context


# Add comment to brand
def addBrandComment(request: HttpRequest):
    if request.user.is_authenticated:
        brand_comment = request.GET.get('brand_comment')
        brand_id = request.GET.get('brand_id')
        parent_id = request.GET.get('parent_id')

        new_comment = BrandsComments(brand_id=brand_id, message=brand_comment,
                                     user_id=request.user.id, parent_id=parent_id)
        new_comment.save()

        context = {
            'comments': BrandsComments.objects.filter(brand_id=brand_id, parent_id=None).order_by(
                '-createDate').prefetch_related('brandscomments_set'),
            'commentCount': BrandsComments.objects.filter(brand_id=brand_id).count()
        }
        return render(request, 'productionsApp/includes/commentsBrand.html', context)


# show categories in side menu
def categories_productions_partial(request: HttpResponse):
    productions_main_categories = CategoryParent.objects.filter(isActive=True)
    siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    context = {
        'siteSettings': siteSettings,
        'main_categories': productions_main_categories
    }
    return render(request, 'productionsApp/includes/categoryPartial.html', context)


# show brands in side menu
def brands_productions_partial(request: HttpResponse):
    productions_brand = ProductsBrand.objects.annotate(productions_count=Count('products')).filter(isActive=True)
    siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    context = {
        'siteSettings': siteSettings,
        'productions_brand': productions_brand
    }
    return render(request, 'productionsApp/includes/brandProduct.html', context)
