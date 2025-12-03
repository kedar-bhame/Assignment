from django.db import models

class User(models.Model):
    # use legacy_id to mirror assignment-provided ids without replacing Django PK
    legacy_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.legacy_id} - {self.name}"

