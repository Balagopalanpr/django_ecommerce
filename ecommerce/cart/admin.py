from django.contrib import admin
from.models import cart,order,Account
from django.http import HttpResponse

# Register your models here.
admin.site.register(cart)
admin.site.register(order)
admin.site.register(Account)
