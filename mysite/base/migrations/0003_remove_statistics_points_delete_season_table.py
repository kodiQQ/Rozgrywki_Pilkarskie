# Generated by Django 5.0.3 on 2024-04-21 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_scorertable_scorer_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='points',
        ),
        migrations.DeleteModel(
            name='Season_Table',
        ),
    ]