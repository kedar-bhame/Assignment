from django.db import models

class Product(models.Model):
    legacy_id = models.IntegerField()
    name = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return f"{self.legacy_id} - {self.name}"
