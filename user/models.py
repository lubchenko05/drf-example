from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=128)
    groups = models.ManyToManyField('CustomUserGroup', related_name='users')


class CustomUserGroup(models.Model):
    name = models.CharField(max_length=256)
