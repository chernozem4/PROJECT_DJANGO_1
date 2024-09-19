from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='clothes')

    def __str__(self):
        return self.name
