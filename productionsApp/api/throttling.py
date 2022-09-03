from rest_framework.throttling import UserRateThrottle

class BrandCommentsThrottle(UserRateThrottle):
    scope = 'brand-comments'

class ProductCommentsThrottle(UserRateThrottle):
    scope = 'product-comments'