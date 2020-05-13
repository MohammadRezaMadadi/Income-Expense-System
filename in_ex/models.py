from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.text}" 


class Income(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.text}" 