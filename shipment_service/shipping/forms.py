from django import forms
from .models import Shipment, POS

class ShipmentForm(forms.ModelForm):
    purchase_orders = forms.ModelMultipleChoiceField(
        queryset=POS.objects.filter(status=POS.READY_FOR_SHIPMENT),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Shipment
        fields = ['destination', 'purchase_orders']


class ShipmentEditForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['destination', 'confirmedOn']