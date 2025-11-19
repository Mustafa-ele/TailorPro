from django.urls import path, include
from rest_framework import routers
from .views import (
    BusinessViewSet, CustomerViewSet, OrderViewSet,
    MeasurementTemplateViewSet, PaymentViewSet,
    dashboard, add_customer, orders_page, order_detail, payments
)

app_name = "orders"

router = routers.DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'measurements', MeasurementTemplateViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    # ---------- PAGES ----------
    path('', dashboard, name='dashboard'),
    path('add-customer/', add_customer, name='add_customer'),
    path('orders/', orders_page, name='orders_page'),
    path('orders/<uuid:pk>/', order_detail, name='order_detail'),
    path('payments/', payments, name='payments'),

    # ---------- API ----------
    path('api/', include(router.urls)),
]
