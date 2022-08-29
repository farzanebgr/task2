from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from contactApp.api.permissions import IsAdminOrReadOnly
from contactApp.api.serializers import SettingSerializer, ContactUsSerializer
from contactApp.models import contactUs
from siteSettingsApp.models import settingModel


# Return the Site Setting model that active in yhe site
class CopyRightAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        setting = settingModel.objects.filter(isMainSettings=True).first()
        serializer = SettingSerializer(setting)
        return Response(serializer.data)

    def post(self, request):
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ContactUsVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = contactUs.objects.all()
    serializer_class = ContactUsSerializer

    def list(self, request, *args, **kwargs):
        empty_field = []
        return Response(empty_field)

    def update(self, request, *args, **kwargs):
        pass
