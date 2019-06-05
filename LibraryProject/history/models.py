from django.db import models


# Create your models here.

class History(models.Model):
    date = models.DateField(null=False, help_text="When did it happen")
    what = models.CharField(null=False, max_length=500, help_text="What happened")
