from django.db import models
from django.urls import reverse


class Player(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    robot_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.robot_name)
    
    def get_absolute_url(self):
        return reverse('hotsite:success-register', kwargs={'pk': self.pk})


class Match(models.Model):
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_one')
    score_player_one = models.IntegerField()
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_two')
    score_player_two = models.IntegerField()
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} x {}'.format(self.player_one.robot_name, self.player_two.robot_name)
