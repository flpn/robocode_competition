from django.db import models
from django.urls import reverse


class Player(models.Model):
    STATE_CHOICES = ((True, 'Sim'), (False, 'Não'),)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    robot_name = models.CharField(max_length=50)
    contributor = models.BooleanField(default=False, verbose_name='Desejo contribuir com o valor de R$ 5,00', choices=STATE_CHOICES)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.robot_name)
    
    def get_absolute_url(self):
        return reverse('hotsite:home', kwargs={'pk': self.pk})


class Match(models.Model):
    CATEGORY_CHOICES = (
        ('groups', 'Fase de grupos'),
        ('16', 'Oitavas de final'),
        ('8', 'Quartas de final'),
        ('4', 'Semi-final'),
        ('2', 'Final'),)

    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_one')
    score_player_one = models.IntegerField()
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_two')
    score_player_two = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='groups')
    date = models.DateField(null=True, blank=True)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)

    def __str__(self):
        return '{} x {}'.format(self.player_one.robot_name, self.player_two.robot_name)
