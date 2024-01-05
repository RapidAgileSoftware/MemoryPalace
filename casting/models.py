from django.db import models


class Actor(models.Model):
    name: str = models.CharField(max_length=200)
    prop: str = models.CharField(max_length=500)
    activity: str = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Role(models.Model):
    acts_as = models.CharField(max_length=5)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.acts_as


class Cast(models.Model):
    title: str = models.CharField(max_length=200)
    roles = models.ManyToManyField(Role)

    # Configure input Translation
    encoding_steps: int = models.IntegerField(default=3)
    contains_numbers: bool = models.BooleanField(default=True)
    contains_letters: bool = models.BooleanField(default=False)
    contains_symbols: bool = models.BooleanField(default=False)
