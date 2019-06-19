from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label='Enter your goals for today', max_length=100,
    widget=forms.TextInput(attrs={ "type":"text", "name":"fname", "placeholder":"Enter your goals for today"}))