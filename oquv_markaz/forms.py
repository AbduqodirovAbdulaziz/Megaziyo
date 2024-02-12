from django import forms
from .models import *


class OquvchiForm(forms.ModelForm):
    class Meta:
        model = Oquvchi
        fields = '__all__'


class TolovForm(forms.ModelForm):
    class Meta:
        model = Tolov
        fields = '__all__'


class GuruhForm(forms.ModelForm):
    class Meta:
        model = Guruh
        fields = '__all__'
