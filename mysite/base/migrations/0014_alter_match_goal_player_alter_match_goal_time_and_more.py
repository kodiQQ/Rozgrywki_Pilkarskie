# Generated by Django 5.0.3 on 2024-05-14 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_match_goal_goal_remove_penalty_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_goal',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.player'),
        ),
        migrations.AlterField(
            model_name='match_goal',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='match_penalty',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.type_of_card'),
        ),
    ]