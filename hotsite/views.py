from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from .models import Player, Match
from .forms import PlayerForm


class HomeView(TemplateView):
    template_name = 'hotsite/home.html'


class SuccessRegisterView(DetailView):
    model = Player


class CreatePlayerView(CreateView):
    form_class = PlayerForm
    template_name = 'hotsite/create_player.html'


class ListMatchesView(ListView):
    def get_queryset(self):
        return Match.objects.all()