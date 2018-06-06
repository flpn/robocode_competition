from django.db import models
from django.urls import reverse


class Stage(models.Model):
    name = models.CharField(max_length=50)
    initial_date = models.DateField(null=True, blank=True)
    final_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    class Meta:
        ordering = ['-score']

    STATE_CHOICES = ((True, 'Sim'), (False, 'Não'),)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    robot_name = models.CharField(max_length=50)
    contributor = models.BooleanField(default=False, verbose_name='Desejo contribuir com o valor de R$ 5,00', choices=STATE_CHOICES)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.robot_name)

    def get_absolute_url(self):
        return reverse('hotsite:home', kwargs={'pk': self.pk})


class Match(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='match_set', null=True, blank=True)
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_one')
    score_player_one = models.IntegerField(default=0)
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_two')
    score_player_two = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)

    def __str__(self):
        return '{} x {}'.format(self.player_one.robot_name, self.player_two.robot_name)
