from django.db import models

# Create your models here.
class TypeContact(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)




