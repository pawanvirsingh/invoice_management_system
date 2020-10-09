from django.db import models


# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.TextField(max_length=25, null=False, blank=False, )
    company_country = models.CharField(max_length=25, null=False, blank=False, )
    company_state = models.CharField(max_length=25, null=False, blank=False, )

    def __str__(self):
        """
           Displays a human-readable representation of Company Model
        """
        return self.company_name


class Customer(models.Model):
    """
       Models for a customer.
    """

    name = models.CharField(max_length=256, null=False, blank=False,
                            help_text='Enter Customer ')
    address = models.TextField(max_length=100, null=True, blank=True,
                               help_text='Enter address of customer or Company'
                               )
    city = models.CharField(max_length=100, null=True, blank=True,
                            help_text='Enter the city of the address')
    state = models.CharField(max_length=50, null=True, blank=True,
                             help_text='Enter the state of the address')
    country = models.CharField(max_length=100, null=True, blank=True,
                               help_text='Enter the country of the address')
    email = models.EmailField(null=True, blank=True,
                              help_text='Enter the email of the customer or \
                              Company')
    mobile = models.EmailField(null=True, blank=True,
                               help_text='Enter the Mobile of the customer or \
                              Company')
    shiping_address = models.TextField(null=True, blank=True)

    def __str__(self):
        """
           Displays a human-readable representation of Customer Model
        """
        return self.name

    def invoices(self):
        """
           Returns all the invoices of a customer.
        """
        return Invoice.objects.filter(customer=self).count()


class Invoice(models.Model):
    PAID = 'paid'
    UNPAID = 'unpaid'
    DRAFT = 'draft'
    OTHERS = 'others'
    INVOICE_STATUS_CHOICES = [
        (PAID, "PAID"),
        (DRAFT, "UNPAID"),
        (DRAFT, 'DRAFT'),
        (OTHERS, 'OTHERS')
    ]

    PROCESSING = 'processing'
    DIGITIZED = 'digitized'
    FAILED = 'failed'
    INVOICE_STATE_CHOICES = [
        (PROCESSING, "Processing"),
        (DIGITIZED, "Digitized"),
        (FAILED, 'Failed'),
    ]

    valid = models.BooleanField(default=True)
    invoice_number = models.CharField(max_length=25,null=True, blank=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    ship_to = models.TextField(null=True, blank=True)
    invoice_state = models.CharField(max_length=10, choices=INVOICE_STATE_CHOICES,default=PROCESSING)
    status = models.CharField(max_length=10, choices=INVOICE_STATUS_CHOICES, default=DRAFT)
    invoice_file = models.FileField(null=True)
    invoice_note = models.TextField(null=True,  blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=False, blank=False),
    next_billing_date = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.invoice_number}"

    def total_items(self):
        total = 0
        items = self.item_set.all()
        for item in items:
            total += item.cost * item.qty
        return total

    def total(self):
        items = self.total_items()
        return items

    def paid(self):
        return self.status == 'Paid'

    def unpaid(self):
        return self.status == 'Unpaid'

    def draft(self):
        return self.status == 'Draft'

    @property
    def items(self):
        return self.item_set.all()


class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    qty = models.IntegerField(default=1)
    unit = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    def total(self):
        return self.cost * self.qty
