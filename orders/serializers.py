from rest_framework import serializers
from .models import Business, Customer, Order, MeasurementTemplate, Payment

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('id','created_at')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('id','created_at')

class OrderSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField(read_only=True)
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.UUIDField(write_only=True, required=True)

    class Meta:
        model = Order
        fields = [
            'id','order_number','business','customer','customer_id','cloth_type',
            'total_amount','advance_paid','balance','delivery_date','status','measurements','notes','created_at'
        ]
        read_only_fields = ('id','created_at','balance')

    def create(self, validated_data):
        customer_id = validated_data.pop('customer_id')
        from .models import Customer
        customer = Customer.objects.get(id=customer_id)
        validated_data['customer'] = customer
        return super().create(validated_data)

class MeasurementTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementTemplate
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('id','created_at')
