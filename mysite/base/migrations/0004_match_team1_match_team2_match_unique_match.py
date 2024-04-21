# Generated by Django 5.0.3 on 2024-04-21 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_statistics_points_delete_season_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1_matches', to='base.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2_matches', to='base.team'),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.UniqueConstraint(fields=('team1', 'team2'), name='unique_match'),
        ),
    ]
