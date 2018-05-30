from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    robot_name = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.robot_name)
