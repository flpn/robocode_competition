from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'email',
            'robot_name',
            'contributor'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'robot_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'email': {
                'unique': 'O email informado já foi cadastrado em nossa base, por favor informe um novo email.'
            },
            'robot_name': {
                'unique': 'Já existe um robô com esse nome. Tente um nome diferente.'
            }
        }
