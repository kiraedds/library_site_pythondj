from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)

