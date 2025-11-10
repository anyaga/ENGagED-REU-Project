from django.db import models


class Profile(models.Model):
    image = None
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    professional_position = models.CharField(max_length=20)
    discipline = models.CharField(max_length=20)
    archetype = models.CharField(max_length=20)

    def __str__(self):
        return f" name={self.name}\n identity={self.identity}\n prof={self.professional_position}"