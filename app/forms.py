from django import forms  
from django.forms.formsets import formset_factory

class GenericDataForm(forms.Form):
    jsondata = forms.CharField()
    pubdate = forms.DateTimeField()

# class BatteryStatusForm(forms.Form):
# 	time = forms.DateTimeField();
# 	value = forms.CharField(max_length=500)

# BatteryStatusFormSet = formset_factory(BatteryStatusForm)
