# Generated by Django 5.0 on 2024-01-03 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0002_alter_actor_acts_as_letter_alter_actor_acts_as_nr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='acts_as_letter',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='acts_as_nr',
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acts_as', models.CharField(max_length=5)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('roles', models.ManyToManyField(to='casting.role')),
            ],
        ),
    ]
