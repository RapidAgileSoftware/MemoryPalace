# Generated by Django 5.0 on 2024-01-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='acts_as_letter',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='acts_as_nr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
