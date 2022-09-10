# Import directly from rest_framework
from rest_framework import viewsets
from rest_framework import serializers
# Import from rest_framework. something
from rest_framework.views import APIView
from rest_framework.response import Response
# Import permission's file from app folder
from productionsApp.api.permissions import IsAdminOrReadOnly
# Import Serializers from serializers' file from app folder
from contactApp.api.serializers import SettingSerializer, ContactUsSerializer
# Import models from apps
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


# Return a form for add message to contact us tabel
class ContactUsVS(viewsets.ModelViewSet):
    queryset = contactUs.objects.all()
    serializer_class = ContactUsSerializer

    def list(self, request, *args, **kwargs):
        return Response(None)

    def update(self, request, *args, **kwargs):
        if request.user.id == self.kwargs['user'].id:
            message = contactUs.objects.get(user_id=request.user.id).all()
            serializer = ContactUsSerializer(message, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(serializers.ValidationError({'error': 'this contact is not yours!'}))

