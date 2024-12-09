from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Entrepreneur'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='network_nodes')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='supplied_by')
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
