from rest_framework import serializers
from app_users.models import CustomUser
from app_core.models import Event, Ticket, Notification

#IMPORTANT: ModelSerializer will automatically generate validators for the serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = CustomUser._meta.fields

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=["event_id",
                "title",
                "description",
                "location",
                "start_time",
                "end_time",
                "organizer",
                "created_at"]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields=["ticket_id",
                "event",
                "participant",
                "purchase_time"]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields=["notification_id",
                "user",
                "message",
                "read",
                "created_at"]
