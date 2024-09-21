from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

@classmethod
def best_clients_past_half_year(cls):
    from django.db.models import Sum
    from django.utils import timezone
    from datetime import timedelta
    
    half_year_ago = timezone.now() - timedelta(days=6 * 30)
    return cls.objects.filter(order_date__gte=half_year_ago) \
        .values('customer__name') \
        .annotate(sum_spent=Sum('total_amount')) \
        .order_by('-sum_spent')[:5]
