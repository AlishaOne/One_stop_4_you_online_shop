from django import forms

from order.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','email','address','zip_code','city']