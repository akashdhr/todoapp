from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label='Enter your goals for today', max_length=100)