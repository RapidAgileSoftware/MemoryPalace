from django.db import models


class Actor(models.Model):
    name: str = models.CharField(max_length=200)
    activity: str = models.CharField(max_length=500)
    prop: str = models.CharField(max_length=500)
    acts_as_nr: int = models.IntegerField(null=True, blank=True)
    acts_as_letter: str = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name
