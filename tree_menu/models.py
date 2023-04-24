from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    

# class Option(models.Model):
#     name = models.CharField(max_length=50)
#     parent = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
#     child = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
#     def __str__(self):
#         return self.name