# event_management_app
# event management API documentation for the given scenarios:

# Events REST API Documentation
View all events
Retrieves a list of all available events.

URL: /api/events
Method: GET
Response Status Code: 200 OK
Response Body: JSON array of events
`
[
    {
        "id": 1,
        "name": "new event create",
        "description": "event create",
        "location": "delhi",
        "is_event_ticket_availabe": true,
        "event_type": "offline",
        "max_seats": 200,
        "booking_open_window_start": "2023-05-14T05:21:55+05:30",
        "booking_open_window_end": "2023-05-17T05:22:00+05:30",
        "created_at": "2023-05-14T05:22:13.440495+05:30",
        "event_date": "2023-05-23T05:22:07+05:30",
        "price": 32,
        "admin": 1
    }
]
`
# Book a ticket for an event

## URL: api/events/{event_id}/book

Method: POST
Request Body: JSON object containing customer information
Response Status Code: 201 Created
Response Body: JSON object containing the created ticket information
`
{
    "id": 5,
    "user": 1,
    "event": 1,
    "timestamp": "2023-05-14T06:13:16.592966+05:30",
    "quantity": 30,
    "total_price": "960.00"
}

`
## View a specific ticket for an event

## URL: api/events/{event_id}/ticket/{ticket_id}
Method: GET
Response Status Code: 200 OK
Response Body: JSON object containing the ticket information
## json response
` [
    {
        "id": 4,
        "user": {
            "id": 1,
            "email": "admin@admin.com",
            "role": "admin",
            "is_active": true
        },
        "event": {
            "id": 1,
            "name": "new event create",
            "description": "event create",
            "location": "delhi",
            "is_event_ticket_availabe": true,
            "event_type": "offline",
            "max_seats": 200,
            "booking_open_window_start": "2023-05-14T05:21:55+05:30",
            "booking_open_window_end": "2023-05-17T05:22:00+05:30",
            "created_at": "2023-05-14T05:22:13.440495+05:30",
            "event_date": "2023-05-23T05:22:07+05:30",
            "price": 32,
            "admin": 1
        },
        "timestamp": "2023-05-14T05:48:47.252851+05:30",
        "quantity": 40,
        "total_price": "1280.00"
    }
]
`

##  View all registered events sorted by event chronologically
## Retrieves a list of all registered events sorted by event date in ascending order.

URL: /events/registered
Method: GET
Response Status Code: 200 OK
Response Body: JSON array of events

`

[
    {
        "id": 1,
        "name": "new event create",
        "description": "event create",
        "location": "delhi",
        "is_event_ticket_availabe": true,
        "event_type": "offline",
        "max_seats": 200,
        "booking_open_window_start": "2023-05-14T05:21:55+05:30",
        "booking_open_window_end": "2023-05-17T05:22:00+05:30",
        "created_at": "2023-05-14T05:22:13.440495+05:30",
        "event_date": "2023-05-23T05:22:07+05:30",
        "price": 32,
        "admin": 1
    },
    {
        "id": 2,
        "name": "event number 2",
        "description": "event des 2",
        "location": "delhi",
        "is_event_ticket_availabe": true,
        "event_type": "offline",
        "max_seats": 4000,
        "booking_open_window_start": "2023-05-20T06:16:00+05:30",
        "booking_open_window_end": "2023-05-31T06:16:00+05:30",
        "created_at": "2023-05-14T06:17:13.141407+05:30",
        "event_date": "2023-06-01T06:17:00+05:30",
        "price": 232343,
        "admin": 1
    }
]
`
## Update an event
## Updates an existing event.

## URL: /api/events/update/{event_id}
Method: PUT
Request Body: JSON object containing updated event information
Response Status Code: 200 OK
Response Body: JSON object containing the updated event information

`
# before update
[
    {
        "id": 1,
        "name": "new event create",
        "description": "event create",
        "location": "delhi",
        "is_event_ticket_availabe": true,
        "event_type": "offline",
        "max_seats": 200,
        "booking_open_window_start": "2023-05-14T05:21:55+05:30",
        "booking_open_window_end": "2023-05-17T05:22:00+05:30",
        "created_at": "2023-05-14T05:22:13.440495+05:30",
        "event_date": "2023-05-23T05:22:07+05:30",
        "price": 32,
        "admin": 1
    }
]

# after update 

{
    "id": 1,
    "name": "event is update for first time",
    "description": "event Description is update for first time",
    "location": "Jaipur",
    "is_event_ticket_availabe": true,
    "event_type": "offline",
    "max_seats": 30,
    "booking_open_window_start": "2023-05-15T06:21:00+05:30",
    "booking_open_window_end": "2023-05-30T06:21:00+05:30",
    "created_at": "2023-05-14T05:22:13.440495+05:30",
    "event_date": "2023-06-02T06:21:00+05:30",
    "price": 7856,
    "admin": 1
}

`


## View a summary of an event
## Retrieves a summary of a specific event.

## URL: /api/events/{event_id}/summary
Method: GET
Response Status Code: 200 OK
Response Body: JSON object containing the event summary information
Example Request Body for Booking a Ticket

## json response 
`{
    "event_name": "new event create",
    "total_tickets": 200,
    "total_earning_from_tickets": 2432,
    "tickets_booked": 76,
    "available_tickets": 124
}
`
# new event create response


## URL: /api/events/create/
Method: GET
Response Status Code: 201 OK
Response Body: JSON object containing the event basic information
Example Request Body for creating a event


`
{
    "id": 2,
    "name": "event number 2",
    "description": "event des 2",
    "location": "delhi",
    "is_event_ticket_availabe": true,
    "event_type": "offline",
    "max_seats": 4000,
    "booking_open_window_start": "2023-05-20T06:16:00+05:30",
    "booking_open_window_end": "2023-05-31T06:16:00+05:30",
    "created_at": "2023-05-14T06:17:13.141407+05:30",
    "event_date": "2023-06-01T06:17:00+05:30",
    "price": 232343,
    "admin": 1
}
`