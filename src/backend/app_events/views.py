from django.views.decorators.http import require_http_methods
from app_core.models import Event, Ticket
from app_users.models import CustomUser
from app_core.serializers import EventSerializer, TicketSerializer
from django.http import JsonResponse
import json
from datetime import datetime

@require_http_methods(['GET'])
def get_all_events(request):
    """Get details about about all the events.

    Args:
        request (dict): request info.

    Returns:
        dict: gives event details of all the events if user is authenticated.
    """
    if request.user.is_authenticated:

        events_queryset = Event.objects.all()
        events_serializer = EventSerializer(events_queryset, many=True)
        data = events_serializer.data

        for row in data:
            row['start_time'] = datetime.fromisoformat(row['start_time']).strftime("%d/%b/%Y at %I:%M%p")
            row['end_time'] = datetime.fromisoformat(row['end_time']).strftime("%d/%b/%Y at %I:%M%p")
            row['organizer'] = CustomUser.objects.get(id= row['organizer']).username 

        #.strftime("%I:%M%p %d%b%Y")
        return JsonResponse({'data': data})
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )

@require_http_methods(['GET'])
def get_all_user_organized_events(request):
    """Get details about all the events organized by the current user, including ticket stats.

    Args:
        request (dict): request info.

    Returns:
        dict: gives event details of all the events organized by the user.
    """
    if request.user.is_authenticated:

        events_queryset = Event.objects.filter(organizer= request.user)
        events_serializer = EventSerializer(events_queryset, many=True)
        data = events_serializer.data

        for row in data:
            row['start_time'] = datetime.fromisoformat(row['start_time']).strftime("%d/%b/%Y at %I:%M%p")
            row['end_time'] = datetime.fromisoformat(row['end_time']).strftime("%d/%b/%Y at %I:%M%p")
            row['organizer'] = CustomUser.objects.get(id= row['organizer']).username 
            row['ticket_count'] = Ticket.objects.filter(event=row['event_id']).count()

        #.strftime("%I:%M%p %d%b%Y")
        return JsonResponse({'data': data})
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def get_event(request):
    """Get details about a particular event.

    Args:
        request (dict): request info containing event id.

    Returns:
        dict: gives event details for the requested event.
    """
    if request.user.is_authenticated:

        try:
            data = json.loads(request.body.decode('utf-8'))
            event_id = data["event_id"]
        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )
        
        event_queryset = Event.objects.get(event_id= event_id)

        events_serializer = EventSerializer(event_queryset)

        data = events_serializer.data
        data['start_time_raw'] = data['start_time']
        data['end_time_raw'] = data['end_time']
        data['start_time'] = datetime.fromisoformat(data['start_time']).strftime("%d/%b/%Y at %I:%M%p")
        data['end_time'] = datetime.fromisoformat(data['end_time']).strftime("%d/%b/%Y at %I:%M%p")
        data['organizer'] = CustomUser.objects.get(id= data['organizer']).username 

        return JsonResponse({'data': data})
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )

@require_http_methods(['POST'])
def book_event_ticket(request):
    """Book a ticket for an event.

    Args:
        request (dict): request info containing event id and user info

    Returns:
        dict: details about the request.
    """
    if request.user.is_authenticated:

        try:
            data = json.loads(request.body.decode('utf-8'))
            event_id = data["event_id"]
            
        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )
        
        
        event_instance = Event.objects.get(event_id= event_id)
        
        new_instance = Ticket(event= event_instance, 
                              participant= request.user)

        # Save the instance to the database
        new_instance.save()

        return JsonResponse({'success': True}, status=201)
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['GET'])
def get_all_user_tickets(request):
    """Get details about all the tickets booked by the current logged in user.

    Args:
        request (dict): request info.

    Returns:
        dict: gives details about all the tickets booked by the current user.
    """
    if request.user.is_authenticated:

        tickets_queryset = Ticket.objects.filter(participant= request.user)
        tickets_serializer = TicketSerializer(tickets_queryset, many=True)
        data = tickets_serializer.data

        for row in data:
            row['purchase_time'] = datetime.fromisoformat(row['purchase_time']).strftime("%d/%b/%Y at %I:%M%p")
            row['event'] = Event.objects.get(event_id= row['event']).title 

        return JsonResponse({'data': data})
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def create_event(request):
    """Adds a new event in the database.

    Args:
        request (dict): request info containing the new event's details.

    Returns:
        dict: Returns conformation on if the task was a success.
    """
    if request.user.is_authenticated and request.user.role == "ORG":

        try:
            data = json.loads(request.body.decode('utf-8'))
            eventTitle= data['eventTitle'] 
            Address= data['Address']
            eventDesc= data['eventDesc']
            startDate= datetime.fromisoformat(data['startDate'])
            endDate= datetime.fromisoformat(data['endDate'])

        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )

        # Create an instance of the model and assign values to its fields
        new_instance = Event(title= eventTitle, 
                             description= eventDesc,
                             location= Address,
                             start_time= startDate,
                             end_time= endDate,
                             organizer= request.user)

        # # Save the instance to the database
        new_instance.save()

        return JsonResponse({'success': True}, status=201)
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def update_event(request):
    """Updates existing event in the database.

    Args:
        request (dict): request info containing the new details of the event.

    Returns:
        dict: Returns conformation on if the task was a success.
    """
    if request.user.is_authenticated and request.user.role == "ORG":

        try:
            data = json.loads(request.body.decode('utf-8'))
            event_id= data['event_id']
            eventTitle= data['eventTitle'] 
            Address= data['Address']
            eventDesc= data['eventDesc']
            startDate= datetime.fromisoformat(data['startDate'])
            endDate= datetime.fromisoformat(data['endDate'])
            
        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )

        model_instance= Event.objects.get(event_id= event_id)

        model_instance.title= eventTitle 
        model_instance.description= eventDesc
        model_instance.location= Address
        model_instance.start_time= startDate
        model_instance.end_time= endDate

        # # Save the instance to the database
        model_instance.save()

        return JsonResponse({'success': True}, status=201)
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def delete_event(request):
    """Deletes an event.

    Args:
        request (dict): request info containing the event's ID.

    Returns:
        dict: Returns conformation on if the task was a success.
    """
    if request.user.is_authenticated and request.user.role == "ORG":

        try:
            data = json.loads(request.body.decode('utf-8'))
            id = data['event_id']

        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )
        
        instance = Event.objects.get(event_id= id)
        instance.delete()

        return JsonResponse({'success': True}, status=201)
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def delete_ticket(request):
    """Deletes a ticket based on ticket ID.

    Args:
        request (dict): request info containing the ticket's ID.

    Returns:
        dict: Returns conformation on if the task was a success.
    """
    if request.user.is_authenticated and request.user.role == "ORG":

        try:
            data = json.loads(request.body.decode('utf-8'))
            id = data['ticket_id']
            print(data)

        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid JSON'}, status=400
            )
        
        instance = Ticket.objects.get(ticket_id= id)
        instance.delete()

        return JsonResponse({'success': True}, status=201)
    
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )