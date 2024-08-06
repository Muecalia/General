from django.db import models
from address_api.models import County
from datetime import datetime as dt
from django.utils import timezone

# Create your models here.
class TypeInstitution(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now())
    #created_date = models.DateTimeField(default=dt.now)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tb_type_institution"
        ordering = ['-created_date']


class Institution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    state = models.BooleanField(default=True)
    type = models.ForeignKey(TypeInstitution, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_institution'
        ordering = ['-created_date']
