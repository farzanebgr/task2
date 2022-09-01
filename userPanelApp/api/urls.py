from rest_framework.routers import DefaultRouter
from django.urls import path, include
from userPanelApp.api import views

urlpatterns = [
    path('user-panel/', views.userPanelDashboard.as_view({'get': 'retrieve'}), name='user-panel'),
    # path('edit-profile/', views.editProdileView.as_view(), name='edit-profile-page'),
    # path('change-password/', views.changePasswordView.as_view(), name='change-password-page'),
    # path('user-basket/', views.userBasket, name='user-basket-page'),
    # path('my-shopping/', views.myShopping.as_view(), name='user-shopping-page'),
    # path('my-shopping-detail/<order_id>', views.myShoppingDetails, name='user-shopping-detail-page'),
    # path('remove-order-detail/', views.remove_order_detail, name='remove-order-detail-ajax'),
    # path('change-order-detail/', views.change_order_detail_count, name='change-order-detail-count-ajax'),
    # path('shopping-paid/', views.shoppingPaid, name='shopping-paid-ajax'),

]
