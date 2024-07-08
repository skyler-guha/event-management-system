# Django API Endpoints Docs

### auth/api/set-csrf-token
* Description: Set the CSRF cookie on the frontend.
* Method: GET
* Request Body Parameters: None

### auth/api/login
* Description: Mark the user as logged in on the backend.
* Method: POST
* Request Body Parameters:
    - username: Username of the user
    - password: Password of the user

### auth/api/logout
* Description: Mark the user as logged out on the backend.
* Method: POST
* Request Body Parameters: None
Django API Endpoints
### events/api/get-all-events
* Description: Get details about about all the events that currently exist in the database.
* Method: GET
* Request Body Parameters: None

### events/api/get-all-user-organized-events
* Description: Get details about all the events organized by the current logged in user, including ticket stats.
* Method: GET
* Request Body Parameters: None

### events/get-event
* Description: Get details about a particular event.
* Method: POST
* Request Body Parameters:
    - event_id: id of the event for which you want details.

### events/api/create-event
* Description: Adds a new event to the database.
* Method: POST
* Request Body Parameters:
    - eventTitle: Title of the event.
    - Address: Location of the event.
    - eventDesc: Description of the event.
    - startDate: Start Date and Time of the event in UTC format.
    - endDate: End Date and Time of the event in UTC format.


### events/api/update-event
* Description: Updates existing event to the database.
* Method: POST
* Request Body Parameters:
    - event_id: Event ID of the event that needs to be updated.
    - eventTitle: Title of the event.
    - Address: Location of the event.
    - eventDesc: Description of the event.
    - startDate: Start Date and Time of the event in UTC format.
    - endDate: End Date and Time of the event in UTC format.

### events/api/delete-event
* Description: Deletes an event.
* Method: POST
* Request Body Parameters:
    - event_id: Event ID of the event that needs to be deleted.

### events/api/book-event-ticket
* Description: Book a ticket for an event for the currently logged in user.
* Method: POST
* Request Body Parameters:
    - event_id: Event ID of the event for which the ticket has to be booked.

### events/api/get-all-user-tickets
* Description: Get details about all the tickets booked by the current logged in user.
* Method: GET
* Request Body Parameters: None

### events/api/delete-ticket
* Description: Deletes a ticket based on ticket ID.
* Method: POST
* Request Body Parameters:
    - ticket_id: Ticket ID of the ticket that needs to be deleted.


