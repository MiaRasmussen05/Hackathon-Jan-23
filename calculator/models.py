from django.db import models

class CalcFunding(models.Model):
    cost = models.IntegerField()
    savings = models.IntegerField()
    salary_pre = models.IntegerField()
    salary_post = models.IntegerField()
    expences = models.IntegerField()

    class Meta:
        ordering = ['cost']

