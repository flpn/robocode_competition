from django.urls import path
from . import views


app_name = 'hotsite'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('usuario/<int:pk>', views.SuccessRegisterView.as_view(), name='success-register'),    
    path('registrar/', views.CreatePlayerView.as_view(), name='create-player'),
    path('partidas/', views.ListMatchesView.as_view(), name='list-matches'),
    path('async_match_list/', views.async_match_list, name='async-match-list'),
]