from django.db import models

# Create your models here.
class Membership(models.Model):
    MEMBERSHIP_CHOICES = ["First Level", "Second Level", "Third Level"]
    membership_type = models.CharField(max_length=None, choices=MEMBERSHIP_CHOICES)