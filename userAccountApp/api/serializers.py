from rest_framework import serializers
from userAccountApp.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password_confirm = self.validated_data['confirm_password']
        if password != password_confirm:
            raise serializers.ValidationError({'error': 'password and confirm should be same!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email is already used!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
