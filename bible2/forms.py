from django import forms

class BibleSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
