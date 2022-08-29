from rest_framework import serializers
from contactApp.models import contactUs
from siteSettingsApp.models import settingModel


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = settingModel
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = contactUs
        exclude = ['isReadByAdmin', 'response', ]

    def validated_fullName(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'error': 'your name and family is too short!!!!'})

    def validated_message(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'error': 'your message is too short!!!!'})

    def validated_user(self, value):
        if value.id.exists():
            return value
        else:
            raise serializers.ValidationError({'error': 'your not access to contact us!!!'})





