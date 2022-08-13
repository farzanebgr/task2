from django.http import HttpRequest, JsonResponse
from productionsApp.models import Products
from orderApp.models import Order, OrderDetail


def addProductToOrder(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Products.objects.filter(id=product_id, isActive=True, isDelete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(isPaid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found'
            })
    else:
        return JsonResponse({
            'status': 'not_auth'
        })
