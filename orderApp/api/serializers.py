from rest_framework import serializers
from rest_framework.response import Response
from productionsApp.models import Products
from orderApp.models import Order, OrderDetail

# Serializer for Sliders in index page
class OrderDetailSerializer(serializers.Serializer):

    # define our necessary fields
    order = serializers.CharField()
    product = serializers.CharField()
    finalPrice = serializers.IntegerField()
    count = serializers.IntegerField()

    def update(self, instance, validated_data):

        # get or create information of order detail or update order detail
        instance.order = validated_data.get('order', instance.order)
        instance.product = validated_data.get('product', instance.product)
        instance.finalPrice = validated_data.get('finalPrice', instance.finalPrice)
        instance.count = validated_data.get('count', instance.count)

        instance.save()
        return instance

    def create(self, validated_data):

        # Create an instance for order detail
        instance =[]
        instance['order'] = validated_data.get('order')
        instance['product'] = validated_data.get('product')
        instance['finalPrice'] = validated_data.get('finalPrice')
        instance['count'] = validated_data.get('count')

        # Check to have correct details
        if instance is not []:
            instance.save()
            return instance

        return Response(serializers.ValidationError({'error': 'The order was not added'}))

    class Meta:
        model = OrderDetail
        fields = ['order', 'product', 'finalPrice', 'count']

    # Validate the number based on input argument
    def validated_count(self, value):
            if value < 1:
                raise serializers.ValidationError({'error': 'The entered number is not valid!'})


    # Validate the number based on the inventory in the database
    def validated_count(self, value, count):
        if value < count:
            raise serializers.ValidationError({'error': 'This product is not available with this number of purchases!'})


