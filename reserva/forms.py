from datetime import date
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data.get('data')
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível agendar em uma data anterior a de hoje')
        return data
    
    def clean_turno(self):
        turno = self.cleaned_data.get('turno')
        data = self.cleaned_data.get('data')        
        reserva_turno = Reserva.objects.filter(data=data, turno=turno).count()
        if reserva_turno >= 2:
            raise forms.ValidationError('Não há agenda disponivel para este turno no momento')
        return turno

    class Meta:
        model = Reserva
        fields = ['nome', 'email', 'data', 'turno', 'tamanho', 'categoria', 'observacoes', 'petshop']
        widgets = {
            'nome': forms.TextInput(
                attrs= {
                    'placeholder': 'Informe o Nome Completo'
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'placeholder': 'Informe um e-mail de contato'
                }
            ),
            'data': forms.DateInput(
                attrs= {
                    'type': 'date'
                }
            ),
            'observacoes': forms.Textarea(
                attrs= {
                    'placeholder': 'Informe aqui detalhes relevantes para a reserva'
                }
            ),
        }