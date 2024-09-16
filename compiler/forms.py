# compiler/forms.py
from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea, label='Enter your code')
    inputs = forms.CharField(widget=forms.Textarea, label='Enter inputs (one per line)', required=False)
