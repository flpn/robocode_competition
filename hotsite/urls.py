from django.urls import path
from . import views


app_name = 'hotsite'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('registrar/', views.CreatePlayerView.as_view(), name='create-player'),
    path('partidas/', views.ListMatchView.as_view(), name='list-matches'),
    path('partidas_grupo/', views.ListMatchByStageView.as_view(), name='list-matches-by-stage'),
    path('classificacao/', views.ListGroupView.as_view(), name='classification-list'),
]
