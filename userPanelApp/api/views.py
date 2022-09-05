from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from userPanelApp.api.serializers import UserSerializer, UserPasswordSerializer
from userAccountApp.models import User


class userPanelDashboard(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChangeProfileGRU(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        u_id = request.user.id
        info = User.objects.filter(pk=u_id).first()
        serializer = UserSerializer(info)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        u_id = request.user.id
        info = User.objects.filter(pk=u_id).first()
        serializer = UserSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ChangePasswordGRU(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserPasswordSerializer

    def retrieve(self, request, *args, **kwargs):
        u_id = request.user.id
        info = User.objects.filter(pk=u_id).first()
        serializer = UserPasswordSerializer(info)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        u_id = request.user.id
        info = User.objects.filter(pk=u_id).first()
        serializer = UserPasswordSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)