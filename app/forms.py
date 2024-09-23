from django import forms

class ResearchForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
