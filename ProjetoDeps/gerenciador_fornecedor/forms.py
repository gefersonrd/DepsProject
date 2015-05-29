from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=100)
    descricao = forms.CharField(widget=forms.Textarea)
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)