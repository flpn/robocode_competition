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
        labels = {
            'name': 'Nome',
            'robot_name': 'Nome do robô',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'robot_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
