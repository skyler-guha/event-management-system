from django.db import models
from django.contrib.auth.models import AbstractUser

#Creating Enum for user roles
class UserRoles(models.TextChoices):
        ORGANIZER = 'ORG',
        PARTICIPANT = 'PAR'

#Extending the default user model by Subclassing AbstractUser
#(Alternatively we could have made a separate profile model with One-To-One relation to default user model)
class CustomUser(AbstractUser):
    role = models.CharField(max_length= 3, blank= False, null= False, 
                            choices= UserRoles.choices, default= UserRoles.PARTICIPANT)

    def __str__(self):
        return self.username
