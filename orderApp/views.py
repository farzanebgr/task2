from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from productionsApp.models import Products


def addProductToOrder(request: HttpRequest):
    product_id = request.GET.get('product_id')
    numbers = request.GET.get('numbers')
    if request.user.is_authenticated:
        product = Products.objects.filter(id=product_id, isDelete=False, isActive=True).first()
        if product is not None:
            pass
    else:
        return JsonResponse({
            'status': 'not_auth'
        })
    print(f'product id is {product_id} and product numbers is {numbers}')

