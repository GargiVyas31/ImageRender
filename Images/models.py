from django.db import models

# Create your models here.
class Content(models.Model):
    data = models.CharField(max_length=100)
    def __str__(self):
        return self.data