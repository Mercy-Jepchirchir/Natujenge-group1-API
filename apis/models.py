from django.db import models

# Create your models here.
MONTH_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)
class Bill(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    month = models.CharField(max_length=200, choices=MONTH_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title

SPECIALITY_CHOICES = (
    ("backend", "Backend"),
    ("frontend", "Frontend"),
    ("fullstack", "Fullstack"),
)

class Team(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255, choices=SPECIALITY_CHOICES)

    def __str__(self):
        return self.name