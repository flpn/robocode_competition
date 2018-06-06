from django.contrib import admin
from .models import Player, Match, Stage, Group


admin.site.register([Player, Match, Stage, Group])
