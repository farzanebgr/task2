from django.urls import path

from userPanelApp import views

urlpatterns = [
    path('user-panel/', views.userPanelDashboard.as_view(), name='user-panel-page'),
    path('edit-profilr/', views.editProdileView.as_view(), name='edit-profile-page'),
    path('change-password/', views.changePasswordView.as_view(), name='change-password-page'),
]