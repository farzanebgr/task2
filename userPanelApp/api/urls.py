from rest_framework.routers import DefaultRouter
from django.urls import path, include
from userPanelApp.api import views

urlpatterns = [
    path('user-panel/', views.userPanelDashboard.as_view(), name='user-panel'),
    path('edit-profile/', views.ChangeProfileGRU.as_view(), name='edit-profile'),
    path('change-password/', views.ChangePasswordGRU.as_view(), name='change-password'),
    path('user-basket/', views.UserBasketGLR.as_view(), name='user-basket'),
    path('user-basket/<int:pk>/', views.UserBasketGUD.as_view(), name='user-basket'),
    # path('my-shopping/', views.myShopping.as_view(), name='user-shopping-page'),
    # path('my-shopping-detail/<order_id>', views.myShoppingDetails, name='user-shopping-detail-page'),
    # path('remove-order-detail/', views.remove_order_detail, name='remove-order-detail-ajax'),
    # path('change-order-detail/', views.change_order_detail_count, name='change-order-detail-count-ajax'),
    # path('shopping-paid/', views.shoppingPaid, name='shopping-paid-ajax'),

]
