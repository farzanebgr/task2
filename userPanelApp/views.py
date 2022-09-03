from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from orderApp.models import Order, OrderDetail
from productionsApp.models import Products
from siteSettingsApp.models import settingModel
from userAccountApp.models import User
from .forms import editProfileModelForm, changePasswordForm
from django.contrib.auth import logout
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class userPanelDashboard(TemplateView):
    template_name = 'userPanelApp/userPanelDashboard.html'

    def get_context_data(self, **kwargs):
        context = super(userPanelDashboard, self).get_context_data()

        # Get site setting model
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['siteSettings'] = siteSettings

        return context

@login_required
def shoppingPaid(request: HttpRequest):
    order_id = request.GET.get('orderId')
    customerCount = int(request.GET.get('customerCount'))
    productCount = int(request.GET.get('productCount'))

    order_item = Order.objects.filter(id=order_id, user_id=request.user.id).first()
    order_detail = OrderDetail.objects.filter(order_id=order_id, order__isPaid=False, order__user_id=request.user.id).first()


    if order_detail is None:
        return JsonResponse({
            'status': 'not_found_detail',
            'icon': 'error',
            'text': 'اطلاعات مربوطه یافت نشد!'
        })
    product = Products.objects.filter(id=order_detail.product.id).first()

    if product.productCount >= customerCount:
        product.productCount -= customerCount
        order_item.isPaid = True
        product.save()
        order_item.save()
        return JsonResponse({
            'status': 'success',
            'icon': 'success',
            'text': 'خرید شما با موفقیت انجام شد',
        })
    else:
        return JsonResponse({
            'status': 'product_not_available',
            'icon': 'warning',
            'text': 'درخواست کالای شما بیش از حد موجودی است.',
        })



@method_decorator(login_required, name='dispatch')
class editProdileView(View):

    def get(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = editProfileModelForm(instance=currentUser)
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()

        context = {
            'form': editForm,
            'currentUser': currentUser,
            'siteSettings': siteSettings
        }
        return render(request, 'userPanelApp/editProfile.html', context)

    def post(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = editProfileModelForm(request.POST, request.FILES, instance=currentUser)
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()

        if editForm.is_valid():
            editForm.save(commit=True)
        context = {
            'form': editForm,
            'currentUser': currentUser,
            'siteSettings': siteSettings
        }
        return render(request, 'userPanelApp/editProfile.html', context)


@method_decorator(login_required, name='dispatch')
class changePasswordView(View):
    def get(self, request: HttpRequest):
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()

        context = {
            'form': changePasswordForm(),
            'siteSettings': siteSettings

        }
        return render(request, 'userPanelApp/changePassword.html', context)

    def post(self, request: HttpRequest):
        form = changePasswordForm(request.POST)
        siteSettings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        if form.is_valid():
            currentUser: User = User.objects.filter(id=request.user.id).first()
            if currentUser.check_password(form.cleaned_data.get('current_password')):
                currentUser.set_password(form.cleaned_data.get('password'))
                currentUser.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('password', 'کلمه عبور فعلی نادرست است')

        context = {
            'form': form,
            'siteSettings': siteSettings
        }
        return render(request, 'userPanelApp/changePassword.html', context)


@method_decorator(login_required, name='dispatch')
class myShopping(ListView):
    model = Order
    template_name = 'userPanelApp/userShopping.html'

    def get_queryset(self):
        queryset = super(myShopping, self).get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(user_id=request.user.id, isPaid=True)
        return queryset


@login_required
def panelPartial(request: HttpRequest):
    return render(request, 'userPanelApp/includes/panelPartial.html')


@login_required
def userBasket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(isPaid=False,
                                                                                             user_id=request.user.id)

    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'userPanelApp/userBasket.html', context)


@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detailId')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__isPaid=False,
                                                             order__user_id=request.user.id).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(isPaid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('userPanelApp/userBasketContent.html', context)
    })


@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detailId')
    state = request.GET.get('state')
    currentCount = request.GET.get('currentCount')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state_or_there_is_no_product_available'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__isPaid=False, order__user_id=request.user.id).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'not_found_detail'
        })
    # product: Products = Products.objects.filter(id=order_detail.product.id)

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()

    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid!'
        })
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(isPaid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('userPanelApp/userBasketContent.html', context)
    })


@login_required
def myShoppingDetails(request: HttpRequest, order_id):
    order = Order.objects.prefetch_related('orderdetail_set').filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('پیدا نشد')
    order_detail = OrderDetail.objects.filter()
    context = {
        'order': order
    }
    return render(request, 'userPanelApp/userShoppingDetail.html', context)
