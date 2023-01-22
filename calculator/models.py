from django.db import models

CHOICES = (('SV', 'Savings'), ('SA', "Salary"))

class CalcFunding(models.Model):
    cost = models.IntegerField()
    savings = models.IntegerField()
    salary_pre = models.IntegerField()
    salary_post = models.IntegerField()
    expences = models.IntegerField()
    fund = models.CharField(max_length=200, choices=CHOICES, default="SV")

    class Meta:
        ordering = ['cost']

