from django.utils import timezone
from rest_framework import serializers
from invoice_management_system.invoice_manager.models import Invoice, Item, Customer, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ("invoice",)

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
         if attrs.get("invoice_file"):
             if attrs.get("invoice_file")._name.split(".")[-1] not in ["PDF",'pdf']:
                 raise  serializers.ValidationError({"invoice_file":"Please upload a pdf file "})
         return attrs

class InvoiceUpdateSerializer(InvoiceSerializer):
    company = CompanySerializer(required=False)
    customer = CustomerSerializers(required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1

    def update(self, instance, validated_data):
        customer_data = validated_data.get('customer')
        items_data = validated_data.pop("items")
        company_data = validated_data.get("company")
        if customer_data:
            Customer.objects.filter(id=instance.customer_id).update(**customer_data)
        if company_data:
            Company.objects.filter(id=instance.company_id).update(**company_data)
        if items_data:
            for item in items_data:
                if item.get("id"):
                    Item.objects.filter(invoice=instance.id,id=item.get("id")).update(**item)
                else:
                    item.update(invoice=instance)
                    Item.objects.create(**item)
        print(instance.__dict__)
        return instance
