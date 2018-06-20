from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from .models import Player, Match, Stage, Group
from .forms import PlayerForm


class HomeView(TemplateView):
    template_name = 'hotsite/home.html'


class CreatePlayerView(SuccessMessageMixin, CreateView):
    form_class = PlayerForm
    template_name = 'hotsite/create_player.html'
    success_message = 'success'


class ListGroupView(ListView):
    template_name = 'hotsite/classification.html'

    def get_queryset(self):
        return Group.objects.all()

class ListMatchView(ListView):
    template_name = 'hotsite/match_list.html'

    def get_queryset(self):
    	return Stage.objects.filter(name__iexact='Fase de Grupos')

    def get_context_data(self, *args, **kwargs):
        context = super(ListMatchView, self).get_context_data(*args, **kwargs)

        return get_match_list_by_group_context(context)


class ListMatchByStageView(ListView):
    template_name = 'hotsite/match_list_ajax.html'

    def get_queryset(self):
        stage_id = self.request.GET.get('stage_id')
        stages_names = {
            'groups': 'Fase de Grupos',
            '16': 'Oitavas de Final',
            '8': 'Quartas de Final',
            '4': 'Semifinal',
            '2': 'Final'
        }

        stage_name = stages_names[stage_id]

        if stage_name:
            return Stage.objects.filter(name__iexact=stage_name)
        else:
            return Stage.objects.filter(name__iexact='Fase de Grupos')

    def get_context_data(self, *args, **kwargs):
        context = super(ListMatchByStageView, self).get_context_data(*args, **kwargs)

        return get_match_list_by_group_context(context)


def get_match_list_by_group_context(context):
    groups = Group.objects.all()
    matches_by_group = {}

    for group in groups:
        matches_by_group[group.name] = Match.objects.filter(player_one__group=group, stage__name='Fase de Grupos')

    context['matches_by_group'] = matches_by_group

    return context
