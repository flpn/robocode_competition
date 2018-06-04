from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from .models import Player, Match
from .forms import PlayerForm


class HomeView(TemplateView):
    template_name = 'hotsite/home.html'


class CreatePlayerView(CreateView):
    form_class = PlayerForm
    template_name = 'hotsite/create_player.html'


class ListMatchesView(ListView):
    template_name = 'hotsite/match_list.html'

    def get_queryset(self):
    	return Match.objects.filter(category__iexact='groups')


def async_match_list(request):
	context = {}

	context['object_list'] = Match.objects.filter(category__iexact='groups')

	if request.method == 'GET':
		category = request.GET.get('category')
		
		if category != None:
			context['object_list'] = Match.objects.filter(category__iexact=category)

	return render(request, 'hotsite/match_list_ajax.html', context)


# ?