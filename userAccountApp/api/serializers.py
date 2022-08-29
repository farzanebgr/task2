from rest_framework import serializers

from userAccountApp.models import User


class RegistrationSerializer(serializers.Serializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data('password')
        password_confirm = self.validated_data('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError({'error': 'password and confirm should be same!'})

        query = User.objects.filter(email=self.validated_data['email'])
        if query.exists():
            raise serializers.ValidationError({'error': 'email is already used!'})

        new_user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        new_user.set_password(password)
        new_user.save()
        return new_user
