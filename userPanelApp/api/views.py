from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from userPanelApp.api.serializers import UserSerializer, UserPasswordSerializer,OrderDetailSerializer,\
UserPanelSerializer
from userAccountApp.models import User
from orderApp.models import OrderDetail
from siteSettingsApp.models import UserPanel


class UserPanelDashboardGL(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = UserPanel.objects.all()
    serializer_class = UserPanelSerializer

class UserPanelDashboardGCRUD(generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,]
    queryset = UserPanel.objects.all()
    serializer_class = UserPanelSerializer

    def retrieve(self, request, *args, **kwargs):
        panel = UserPanel.objects.filter(pk=self.kwargs['id']).first()
        serializer = UserPanelSerializer(panel)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        p_id = self.kwargs['id']
        panel = UserPanel.objects.filter(pk=p_id).first()
        serializer = UserPanelSerializer(panel, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = UserPanelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        p_id = self.kwargs['id']
        panel = UserPanel.objects.filter(pk=p_id).first()
        panel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        if serializer.is_valid(raise_exception=True):
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
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class UserBasketGLR(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def list(self, request, *args, **kwargs):
        u_id = request.user.id
        info = OrderDetail.objects.filter(order__isPaid=False, order__user_id=u_id).all()
        serializer = OrderDetailSerializer(info, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class UserBasketGUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        u_id = request.user.id
        pk = self.kwargs['pk']
        info = OrderDetail.objects.filter(order__isPaid=False, order__user_id=u_id, pk=pk).first()
        serializer = OrderDetailSerializer(info)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        u_id = request.user.id
        pk = self.kwargs['pk']
        info = OrderDetail.objects.filter(order__isPaid=False, order__user_id=u_id,pk=pk).first()
        serializer = OrderDetailSerializer(info, data=request.data)
        if serializer.is_valid(raise_exception=True):
             serializer.save()
             return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        u_id = request.user.id
        pk = self.kwargs['pk']
        info = OrderDetail.objects.filter(order__isPaid=False, order__user_id=u_id, pk=pk).first()
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)