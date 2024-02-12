from django.db import models
from concerts.models import Concert
from persons.models import Person
from django.contrib.auth.models import User

class Ticket(models.Model):
    seat_number = models.IntegerField()
    gate_number = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="tickets")
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name="tickets")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets", default=1)

def __str__(self):
    return f"Ticket for {self.user.username}"

