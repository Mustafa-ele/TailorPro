from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add-customer/", views.add_customer, name="add_customer"),
    path("measurements/", views.measurements, name="measurements"),
    path("orders/", views.orders_page, name="orders_page"),
    path("pending-orders/", views.pending_orders, name="pending_orders"),
    path("completed-orders/", views.completed_orders, name="completed_orders"),
    path("payments/", views.payments, name="payments"),
]
