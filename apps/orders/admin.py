from django.contrib import admin
from apps.orders.models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'store',
        'name_customer',
        'phone',
        'address',
        'total',
        'status',
        'created_at',
    ]
    search_fields = [
        'phone',
        'created_at',
    ]