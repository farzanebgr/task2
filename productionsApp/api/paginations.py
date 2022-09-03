from rest_framework.pagination import PageNumberPagination

class ProductListPagination(PageNumberPagination):
    page_size = 6

class BrandListPagination(PageNumberPagination):
    page_size = 2


