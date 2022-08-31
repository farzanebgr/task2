from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from userAccountApp.api.serializers import RegistrationSerializer
# from userAccountApp.models import User


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
