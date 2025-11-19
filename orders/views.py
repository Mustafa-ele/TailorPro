<<<<<<< HEAD
# orders/views.py
from rest_framework import viewsets, filters
from .models import Business, Customer, Order, MeasurementTemplate, Payment
from .serializers import (
    BusinessSerializer, CustomerSerializer,
    OrderSerializer, MeasurementTemplateSerializer,
    PaymentSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import action

# --- API ViewSets (unchanged) ---
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().order_by('-created_at')
    serializer_class = BusinessSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','owner_name','phone']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('customer','business').all().order_by('-created_at')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number','customer__name','customer__phone']

    @action(detail=True, methods=['post'])
    def send_whatsapp(self, request, pk=None):
        order = self.get_object()
        text = f"Hi {order.customer.name}, your order {order.order_number} ({order.cloth_type}) is {order.status}. Delivery: {order.delivery_date}. Balance: {order.balance}"
        wa_link = f"https://wa.me/{order.customer.phone}?text={text.replace(' ','%20')}"
        return Response({"wa_link": wa_link, "text": text})

class MeasurementTemplateViewSet(viewsets.ModelViewSet):
    queryset = MeasurementTemplate.objects.all().order_by('-created_at')
    serializer_class = MeasurementTemplateSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-created_at')
    serializer_class = PaymentSerializer

# -------------------------------
# HTML PAGE VIEWS (Dashboard UI)
# -------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CustomerForm, OrderForm, PaymentForm
from django.contrib import messages
from django.db.models import Q
from .models import OrderStatusHistory


def dashboard(request):
    customers_count = Customer.objects.count()
    orders_count = Order.objects.count()
    pending_orders = Order.objects.filter(status__in=['RECEIVED','CUTTING','STITCHING']).count()
    recent_orders = Order.objects.select_related('customer').order_by('-created_at')[:6]
    context = {
        "customers_count": customers_count,
        "orders_count": orders_count,
        "pending_orders": pending_orders,
        "recent_orders": recent_orders,
    }
    return render(request, "orders/dashboard.html", context)

# Add Customer (GET shows form, POST saves)
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer created.")
            return redirect(reverse('orders:dashboard'))
    else:
        form = CustomerForm()
    return render(request, "orders/add_customer.html", {"form": form})

# Orders list + create via form modal
def orders_page(request):
    q = request.GET.get('q','')
    orders = Order.objects.select_related('customer').order_by('-created_at')
    if q:
        orders = orders.filter(Q(order_number__icontains=q) | Q(customer__name__icontains=q) | Q(customer__phone__icontains=q))
    # handle create order POST
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order created.")
            return redirect(reverse('orders:orders_page'))
    else:
        form = OrderForm()
    return render(request, "orders/orders.html", {"orders": orders, "form": form, "q": q})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    # ---------------------
    # STATUS UPDATE BLOCK
    # ---------------------
    if request.method == "POST" and "update_status" in request.POST:
        new_status = request.POST.get("status")
        if new_status:
            order.status = new_status
            order.save()

            # save to status history
            OrderStatusHistory.objects.create(
                order=order,
                status=new_status
            )

            messages.success(request, "Order status updated.")
            return redirect(reverse('orders:order_detail', args=[order.id]))

    # ---------------------
    # PAYMENT BLOCK
    # ---------------------
    if request.method == "POST" and "mark_paid" in request.POST:
        amount = request.POST.get("amount")
        method = request.POST.get("method")
        txid = request.POST.get("transaction_id")

        if amount:
            Payment.objects.create(
                order=order,
                amount=amount,
                method=method,
                transaction_id=txid,
                status="COMPLETED"
            )

            order.advance_paid = float(order.advance_paid) + float(amount)
            order.save()

            messages.success(request, "Payment recorded.")
            return redirect(reverse('orders:order_detail', args=[order.id]))

    # ---------------------
    # WHATSAPP LINK
    # ---------------------
    text = (
        f"Hi {order.customer.name}, your order {order.order_number} "
        f"({order.cloth_type}) is {order.status}. "
        f"Delivery: {order.delivery_date}. Balance: {order.balance}"
    )

    wa_link = f"https://wa.me/{order.customer.phone}?text={text.replace(' ','%20')}"

    return render(request, "orders/order_detail.html", {
        "order": order,
        "wa_link": wa_link
    })





def payments(request):
    payments = Payment.objects.select_related('order').order_by('-created_at')
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment recorded.")
            return redirect(reverse('orders:payments'))
    else:
        form = PaymentForm()
    return render(request, "orders/payments.html", {"payments": payments, "form": form})
=======
# orders/views.py
from rest_framework import viewsets, filters
from .models import Business, Customer, Order, MeasurementTemplate, Payment
from .serializers import (
    BusinessSerializer, CustomerSerializer,
    OrderSerializer, MeasurementTemplateSerializer,
    PaymentSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import action

# --- API ViewSets (unchanged) ---
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().order_by('-created_at')
    serializer_class = BusinessSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','owner_name','phone']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('customer','business').all().order_by('-created_at')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number','customer__name','customer__phone']

    @action(detail=True, methods=['post'])
    def send_whatsapp(self, request, pk=None):
        order = self.get_object()
        text = f"Hi {order.customer.name}, your order {order.order_number} ({order.cloth_type}) is {order.status}. Delivery: {order.delivery_date}. Balance: {order.balance}"
        wa_link = f"https://wa.me/{order.customer.phone}?text={text.replace(' ','%20')}"
        return Response({"wa_link": wa_link, "text": text})

class MeasurementTemplateViewSet(viewsets.ModelViewSet):
    queryset = MeasurementTemplate.objects.all().order_by('-created_at')
    serializer_class = MeasurementTemplateSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-created_at')
    serializer_class = PaymentSerializer

# -------------------------------
# HTML PAGE VIEWS (Dashboard UI)
# -------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CustomerForm, OrderForm, PaymentForm
from django.contrib import messages
from django.db.models import Q
from .models import OrderStatusHistory


def dashboard(request):
    customers_count = Customer.objects.count()
    orders_count = Order.objects.count()
    pending_orders = Order.objects.filter(status__in=['RECEIVED','CUTTING','STITCHING']).count()
    recent_orders = Order.objects.select_related('customer').order_by('-created_at')[:6]
    context = {
        "customers_count": customers_count,
        "orders_count": orders_count,
        "pending_orders": pending_orders,
        "recent_orders": recent_orders,
    }
    return render(request, "orders/dashboard.html", context)

# Add Customer (GET shows form, POST saves)
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer created.")
            return redirect(reverse('orders:dashboard'))
    else:
        form = CustomerForm()
    return render(request, "orders/add_customer.html", {"form": form})

# Orders list + create via form modal
def orders_page(request):
    q = request.GET.get('q','')
    orders = Order.objects.select_related('customer').order_by('-created_at')
    if q:
        orders = orders.filter(Q(order_number__icontains=q) | Q(customer__name__icontains=q) | Q(customer__phone__icontains=q))
    # handle create order POST
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order created.")
            return redirect(reverse('orders:orders_page'))
    else:
        form = OrderForm()
    return render(request, "orders/orders.html", {"orders": orders, "form": form, "q": q})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    # ---------------------
    # STATUS UPDATE BLOCK
    # ---------------------
    if request.method == "POST" and "update_status" in request.POST:
        new_status = request.POST.get("status")
        if new_status:
            order.status = new_status
            order.save()

            # save to status history
            OrderStatusHistory.objects.create(
                order=order,
                status=new_status
            )

            messages.success(request, "Order status updated.")
            return redirect(reverse('orders:order_detail', args=[order.id]))

    # ---------------------
    # PAYMENT BLOCK
    # ---------------------
    if request.method == "POST" and "mark_paid" in request.POST:
        amount = request.POST.get("amount")
        method = request.POST.get("method")
        txid = request.POST.get("transaction_id")

        if amount:
            Payment.objects.create(
                order=order,
                amount=amount,
                method=method,
                transaction_id=txid,
                status="COMPLETED"
            )

            order.advance_paid = float(order.advance_paid) + float(amount)
            order.save()

            messages.success(request, "Payment recorded.")
            return redirect(reverse('orders:order_detail', args=[order.id]))

    # ---------------------
    # WHATSAPP LINK
    # ---------------------
    text = (
        f"Hi {order.customer.name}, your order {order.order_number} "
        f"({order.cloth_type}) is {order.status}. "
        f"Delivery: {order.delivery_date}. Balance: {order.balance}"
    )

    wa_link = f"https://wa.me/{order.customer.phone}?text={text.replace(' ','%20')}"

    return render(request, "orders/order_detail.html", {
        "order": order,
        "wa_link": wa_link
    })





def payments(request):
    payments = Payment.objects.select_related('order').order_by('-created_at')
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment recorded.")
            return redirect(reverse('orders:payments'))
    else:
        form = PaymentForm()
    return render(request, "orders/payments.html", {"payments": payments, "form": form})
>>>>>>> 25ebfac29b52da4c94d0490e2f97baf08cb66efc
