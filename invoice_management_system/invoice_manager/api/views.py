from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import ModelViewSet

from invoice_management_system.invoice_manager.api.serializers import InvoiceSerializer

from invoice_management_system.invoice_manager.models import Invoice


class InvoiceViewset(ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Invoice.objects.all()

