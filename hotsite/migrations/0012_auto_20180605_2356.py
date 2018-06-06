# Generated by Django 2.0.5 on 2018-06-06 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotsite', '0011_player_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_set', to='hotsite.Stage'),
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='robot_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
