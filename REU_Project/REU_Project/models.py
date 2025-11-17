from django.db import models


class Profile(models.Model):
    image                 = models.ImageField(upload_to='avatar/', blank=True, null=True)
    name                  = models.CharField(max_length=20)
    identity              = models.CharField(max_length=20)
    professional_position = models.CharField(max_length=20)
    discipline            = models.CharField(max_length=20)
    archetype             = models.CharField(max_length=20)

    def __str__(self):
        sub1 = f"name={self.name}\n identity={self.identity}\n prof={self.professional_position}"
        sub2 = f"discipline={self.discipline}\narchetype={self.archetype}\n\n"
        return sub1 + sub2
    


class Download(models.Model):
    email = models.EmailField()
    pdf   = models.CharField(max_length=255)
    time  = models.DateTimeField(auto_now_add=True)