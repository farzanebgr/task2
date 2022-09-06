# Import directly from rest_framework
from rest_framework import serializers
# Import models from apps
from contactApp.models import contactUs
from siteSettingsApp.models import settingModel

# Serializer for settingModel to show data from database
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = settingModel
        fields = "__all__"

# Serializer for contactUs to validate data for send them to database
class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = contactUs
        exclude = ['isReadByAdmin', 'response', ]
    # Validate fullname for send it to database if it was valid
    def validated_fullName(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'error': 'your name and family is too short!!!!'})
    # Validate message for send it to database if it was valid
    def validated_message(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'error': 'your message is too short!!!!'})
    # Validate user for send it was login in site
    def validated_user(self, value):
        if value.id.exists():
            return value
        else:
            raise serializers.ValidationError({'error': 'your not access to contact us!!!'})





