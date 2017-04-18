from django import forms  

class GenericDataForm(forms.Form):
    jsondata = forms.CharField(max_length=100)
    pubdate = forms.DateTimeField()
