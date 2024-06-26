from django.db import models
from shop.models import product
from django.contrib.auth.models import User

# Create your models here.
class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    orderd_date = models.DateTimeField(auto_now_add=True)
    phone=models.BigIntegerField()
    address=models.TextField()
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    def __str__(self):
        return self.user.username

class Account(models.Model):
    acctnum=models.BigIntegerField()
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str (self.acctnum)


