from django.db import models
from app_users.models import CustomUser

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length= 1000)
    location = models.CharField(max_length= 100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete= models.CASCADE) 
    participant = models.ForeignKey(CustomUser, on_delete= models.CASCADE) 
    purchase_time = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE) 
    message = models.CharField(max_length= 500)
    read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)