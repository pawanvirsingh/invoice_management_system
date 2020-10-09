from django.contrib import admin
from invoice_management_system.invoice_manager.models import *


admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(Company)
admin.site.register(Customer)

