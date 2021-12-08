from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return "{} | {}".format(self.title, self.user)


class Income(models.Model):

    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)    