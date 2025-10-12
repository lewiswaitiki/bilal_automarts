from django import forms
from .models import Vehicle, VehicleImage
from django.forms import modelformset_factory

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'  # or list specific fields if you want control


class VehicleImageForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ['image', 'caption']

VehicleImageFormSet = modelformset_factory(
    VehicleImage,
    form=VehicleImageForm,
    extra=3,  # Show 3 image fields by default
    max_num=10,
)


class VehicleInquiryForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')