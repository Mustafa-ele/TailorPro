from django.shortcuts import render
from orders.models import Customer, Order

def dashboard(request):
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    ready_orders = Order.objects.filter(status="READY").count()
    delivered_orders = Order.objects.filter(status="DELIVERED").count()

    latest_orders = Order.objects.select_related("customer").order_by('-created_at')[:5]

    context = {
        "total_customers": total_customers,
        "total_orders": total_orders,
        "ready_orders": ready_orders,
        "delivered_orders": delivered_orders,
        "latest_orders": latest_orders,
    }
    return render(request, "orders/dashboard.html", context)

