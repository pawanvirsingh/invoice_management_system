from django.utils import timezone
from rest_framework import serializers

from invoice_management_system.invoice_manager.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    # invoci_i

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1


