from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from bhp_personnel.models import Employee
from bhp_personnel.models.department import Department


class Position(models.Model):
    """
    Position table made as a separate table so that the employee positions can be added to the database
    dynamically
    """
    name = models.CharField(max_length=50)


class Personnel(Employee):
    """
    Personnel can only have one position, in the event that an employee have two positions,
    in the position table add the positions joined with a dash. e.g. supervisor-accountant
    """
    position = models.OneToOneField(Position, on_delete=models.CASCADE)

