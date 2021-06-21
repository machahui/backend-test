from django.db import models
from django.utils import timezone
# Create your models here.

class Empresa(models.Model):
    name = models.CharField(max_length=100)
    vat = models.CharField(max_length=20)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name