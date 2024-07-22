from django.db import models


class Product(models.Model):
    """Product model for Product objects"""
    name = models.CharField(max_length=100, verbose_name='Product name')
    model = models.CharField(max_length=50, verbose_name='Product model')
    release_date = models.DateField(verbose_name='Product release date')

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Network(models.Model):
    """Network model for Network objects"""
    TYPE_CHOICES = [
        ('F', 'Factory'),
        ('R', 'Retail Network'),
        ('I', 'Individual Entrepreneur'),
    ]

    name = models.CharField(max_length=100, verbose_name='Network name')

    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Country')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    house_number = models.CharField(max_length=10, verbose_name='House number')
    # equipment supplier key is self because other networks will be created in this model
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='supplied_by',
                                 verbose_name='Supplier')

    # networks can have many products key is Product model
    products = models.ManyToManyField(Product, blank=True, related_name='networks', verbose_name='Products')

    # debt to supplier with cents
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                                           verbose_name='Debt for supplier')
    # created time automatic set now when created
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    # level of network that how many suppliers was started from factory
    level = models.PositiveIntegerField(default=0, verbose_name='Hierarchy Level', editable=False)
    # three types of networks Factory, Retail Network, Individual Entrepreneur
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F', verbose_name='Network Type')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # function for automatic set level of net
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0

        # validator that debt cannot be negative
        if self.debt_to_supplier < 0:
            raise ValueError("Debt cannot be negative.")

        # ensure that 'type' is valid
        if self.type not in dict(self.TYPE_CHOICES).keys():
            raise ValueError("Invalid network type.")

        # if network has no supplier then it will not have any debt
        if self.debt_to_supplier and self.supplier is None:
            raise ValueError("If no supplier, then no debt")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'
        ordering = ['level', 'name']
