from django.http import HttpRequest, JsonResponse
from productionsApp.models import Products
from orderApp.models import Order, OrderDetail


def addProductToOrder(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    product_count = int(request.GET.get('productCount'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'تعداد وارد شده معتبر نمی باشد',
            'confirm_button_text': 'اوکی تغییرش میدم',
            'icon': 'warning'
        })
    if product_count < count:
        return JsonResponse({
            'status': 'there_is_no_product',
            'text': 'تعداد وارد شده برای این محصول در انبار موجود نمی باشد',
            'confirm_button_text': 'اوکی کمترش چی؟',
            'icon': 'error'
        })

    if request.user.is_authenticated:
        product = Products.objects.filter(id=product_id, isActive=True, isDelete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(isPaid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                # current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'حله...',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'متوجهم',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'وارد شم!',
            'icon': 'info'
        })
