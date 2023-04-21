from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)