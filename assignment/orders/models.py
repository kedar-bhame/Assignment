from django.db import models

class Order(models.Model):
    legacy_id = models.IntegerField()
    user_legacy_id = models.IntegerField()
    product_legacy_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.legacy_id}"
