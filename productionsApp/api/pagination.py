from rest_framework.pagination import PageNumberPagination

class ProductListPagination(PageNumberPagination):
    # Number of products on a page
    page_size = 6

    # instead of the name page for the page parameter
    page_query_param = 'product-page'

    # an other parameter for pagination
    page_size_query_param  = 'size'

    # Maximum product per page
    max_page_size = 6



class BrandListPagination(PageNumberPagination):
    # Number of brand on a page
    page_size = 2

    # instead of the name page for the page parameter
    page_query_param = 'brand-page'

    # Maximum product per page
    max_page_size = 2



