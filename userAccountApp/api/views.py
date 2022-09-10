from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin
from userAccountApp.api.serializers import RegistrationSerializer

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class TokenBlacklistView(BlacklistMixin):
    def blacklist(self):
        token = RefreshToken(base64_encoded_token_string)
        token.blacklist()