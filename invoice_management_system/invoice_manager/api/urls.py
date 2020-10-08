from rest_framework.routers import SimpleRouter

from invoice_management_system.invoice_manager.api import views


router = SimpleRouter()

router.register(r'invoice', views.InvoiceViewset, basename='invoice')
router.register(r'item', views.ItemViewset, basename='item')
