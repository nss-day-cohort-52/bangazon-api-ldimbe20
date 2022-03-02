from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

 
  