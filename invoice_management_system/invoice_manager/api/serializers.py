
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
    items = ItemSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
        if attrs.get("invoice_file"):
            if attrs.get("invoice_file")._name.split(".")[-1] not in ["PDF", 'pdf']:
                raise serializers.ValidationError({"invoice_file": "Please upload a pdf file "})

        # adding mock data
        mock_customer_data = {
            "name": "pawanvir singhn10",
            "address": "Pawan",
            "city": "Delho",
            "state": "Delhi",
            "country": "INdia",
            "email": "pawanvir.singh26@gmail.com",
            "mobile": "pawanvir.singh26@gmail.com",
            "shiping_address": "Seector 40"
        }
        customer = Customer.objects.create(**mock_customer_data)
        attrs["customer"] = customer
        # for company
        mock_comapany_data = {
            "company_name": "pju",
            "company_address": "Sector 40 Gurugram",
            "company_country": "India",
            "company_state": "Haryana"
        }
        attrs["company"] = Company.objects.create(**mock_comapany_data)
        return attrs

    def save(self, **kwargs):
        super(InvoiceSerializer, self).save()
        #adding data for invoice
        item_data = {
            "name": "pawanvir singh",
            "description": "qwe",
            "cost": "100.00",
            "qty": 1,
            "unit": "rs",
            "invoice" : self.instance
        }
        Item.objects.create(**item_data)
        return self.instance


class InvoiceUpdateSerializer(InvoiceSerializer):
    # company = CompanySerializer(required=False)
    # customer = CustomerSerializers(required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
        customer_data = attrs.get('customer')
        company_data = attrs.get("company")
        if customer_data:
            Customer.objects.filter(id=self.instance.customer_id).update(**customer_data)
        if company_data:
            Company.objects.filter(id=self.instance.company_id).update(**company_data)
        return attrs

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items")
        super(InvoiceUpdateSerializer, self).update(instance, validated_data)
        if items_data:
            for item in items_data:
                if item.get("id"):
                    Item.objects.filter(invoice=instance.id, id=item.get("id")).update(**item)
                else:
                    item.update(invoice=instance)
                    Item.objects.create(**item)
        return instance
