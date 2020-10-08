
from rest_framework.permissions import AllowAny

from rest_framework.viewsets import ModelViewSet,GenericViewSet

from invoice_management_system.invoice_manager.api.serializers import InvoiceSerializer, InvoiceUpdateSerializer, \
    ItemSerializer
from invoice_management_system.invoice_manager.authentication import TokenAuthentication

from invoice_management_system.invoice_manager.models import Invoice, Item
from invoice_management_system.invoice_manager.permissions import RolePermission
from rest_framework import mixins

class InvoiceViewset(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = (RolePermission,)
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Invoice.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["GET","POST"]:
            return InvoiceSerializer
        return InvoiceUpdateSerializer



class ItemViewset(GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = ItemSerializer
    permission_classes = (AllowAny)

    def get_queryset(self):
        return Item.objects.all()
