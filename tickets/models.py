from django.db import models
from concerts.models import Concert
from persons.models import Person
from django.contrib.auth.models import User

class Ticket(models.Model):
    seat_number = models.IntegerField()
    gate_number = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE,null=True)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return f"Ticket for {self.user.get_full_name()}"

