from django.db import models
from django.urls import reverse


class Stage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    initial_date = models.DateField(null=True, blank=True, verbose_name='Data inicial')
    final_date = models.DateField(null=True, blank=True, verbose_name='Data final')

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.name


class Player(models.Model):
    class Meta:
        ordering = ['-score']
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    STATE_CHOICES = ((True, 'Sim'), (False, 'Não'),)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Grupo', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(unique=True)
    robot_name = models.CharField(max_length=50, unique=True, verbose_name='Nome do robô')
    contributor = models.BooleanField(default=True, verbose_name='Desejo contribuir com o valor de R$ 5,00', choices=STATE_CHOICES)
    score = models.IntegerField(default=0, verbose_name='Pontuação')

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.robot_name)

    def get_absolute_url(self):
        return reverse('hotsite:home', kwargs={})


class Match(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name='Etapa', related_name='match_set', null=True, blank=True)
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Jogador 1', related_name='player_one')
    score_player_one = models.IntegerField(default=0, verbose_name='Placar do jogador 1')
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Jogador 2', related_name='player_two')
    score_player_two = models.IntegerField(default=0, verbose_name='Placar do jogador 2')
    date = models.DateField(null=True, blank=True, verbose_name='Data')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Vencedor', related_name='winner', null=True, blank=True)

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return '{} x {}'.format(self.player_one.robot_name, self.player_two.robot_name)
