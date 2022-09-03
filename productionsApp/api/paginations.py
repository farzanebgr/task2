from rest_framework.pagination import LimitOffsetPagination

class BrandListPagination(LimitOffsetPagination):
    PAGE_SIZE =2