from django import forms
from base.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder':'Informe o Nome Completo'
                }
                ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Informe um E-mail de contato'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder':'Escreva sua mensagem'
                }
            ),
        }
