from django.urls import path
from . import views

urlpatterns = [
    path('api/get-all-events', views.get_all_events, name='get_all_events'),
    path('api/get-all-user-organized-events', views.get_all_user_organized_events, name='get_all_user_organized_events'),
    path('api/get-event', views.get_event, name='get_event'),
    path('api/create-event', views.create_event, name='create_event'),
    path('api/update-event', views.update_event, name='update_event'),
    path('api/delete-event', views.delete_event, name='delete_event'),
    path('api/book-event-ticket', views.book_event_ticket, name='book_event_ticket'),
    path('api/get-all-user-tickets', views.get_all_user_tickets, name='get_all_user_tickets'),
    path('api/delete-ticket', views.delete_ticket, name='delete_ticket'),
]

