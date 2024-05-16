# Generated by Django 5.0.3 on 2024-04-21 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_match_team1_match_team2_match_unique_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.league'),
        ),
        migrations.CreateModel(
            name='season_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.league')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.team')),
            ],
        ),
    ]