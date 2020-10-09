from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from invoice_management_system.invoice_manager.api.urls import router as invoice_router

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()



app_name = "api"
urlpatterns = invoice_router.urls

