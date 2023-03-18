from django.db import models


class RegisterModel(models.Model):
    city = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
