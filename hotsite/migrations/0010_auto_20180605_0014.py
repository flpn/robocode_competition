# Generated by Django 2.0.5 on 2018-06-05 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotsite', '0009_match_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('initial_date', models.DateField(blank=True, null=True)),
                ('final_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-score']},
        ),
        migrations.RemoveField(
            model_name='match',
            name='category',
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_player_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_player_two',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='hotsite.Stage'),
        ),
    ]