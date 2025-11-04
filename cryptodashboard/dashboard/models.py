from django.db import models
from django.contrib.auth.models import User

class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    
    def __str__(self):
        return f"{self.user.username}'s {self.amount} of {self.coin_id}"