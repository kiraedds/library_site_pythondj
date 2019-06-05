from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthYear = models.PositiveSmallIntegerField(help_text="Authors' year of birth")
    facePhoto = models.URLField(help_text="URL to authors' photo")

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)
