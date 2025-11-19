# orders/forms.py
from django import forms
from .models import Customer, Order, Payment, MeasurementTemplate

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['business','name','phone','address','notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows':2}),
        }

class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    delivery_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Order
        fields = ['order_number','business','customer','cloth_type','total_amount','advance_paid','delivery_date','status','measurement_data','notes']
        widgets = {
            'measurement_data': forms.Textarea(attrs={'rows':2}),
            'notes': forms.Textarea(attrs={'rows':2}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'method', 'transaction_id', 'status']
        widgets = {
            'method': forms.Select(attrs={'class':'form-control'}),
            'transaction_id': forms.TextInput(attrs={'placeholder':'UPI Ref / Bank Txn ID'}),
        }

