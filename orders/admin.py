<<<<<<< HEAD
from django.contrib import admin
from .models import Business, Customer, Order, MeasurementTemplate, Payment

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name','owner_name','phone','plan','created_at')
    search_fields = ('name','owner_name','phone')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone','business')
    search_fields = ('name','phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','customer','cloth_type','status','delivery_date','total_amount','advance_paid')
    list_filter = ('status','cloth_type')
    search_fields = ('order_number','customer__name','customer__phone')

@admin.register(MeasurementTemplate)
class MeasurementTemplateAdmin(admin.ModelAdmin):
    list_display = ('name','business')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order','amount','method','status','created_at')
=======
from django.contrib import admin
from .models import Business, Customer, Order, MeasurementTemplate, Payment

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name','owner_name','phone','plan','created_at')
    search_fields = ('name','owner_name','phone')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone','business')
    search_fields = ('name','phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','customer','cloth_type','status','delivery_date','total_amount','advance_paid')
    list_filter = ('status','cloth_type')
    search_fields = ('order_number','customer__name','customer__phone')

@admin.register(MeasurementTemplate)
class MeasurementTemplateAdmin(admin.ModelAdmin):
    list_display = ('name','business')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order','amount','method','status','created_at')
>>>>>>> 25ebfac29b52da4c94d0490e2f97baf08cb66efc
