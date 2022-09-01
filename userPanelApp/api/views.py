from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from productionsApp.api.permissions import IsAdminOrReadOnly
from userPanelApp.api.serializers import UserSerializer
from userAccountApp.models import User
from siteSettingsApp.models import settingModel


class userPanelDashboard(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
