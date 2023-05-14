from django.urls import path 
from event_app.views import (
    EventListView,
    BookEventTicket,
    BookTicketView,
    RegisteredEventsList,
    EventCreateAdmin,
    EventUpdateAdmin,
    EventSummaryAdmin

)
'''
    /events [GET] - View all events
    /events/{event_id}/book [POST] - Book a ticket for an event
    /events/{event_id}/ticket/{ticket_id} [GET] - View a specific ticket for an event

    /events/registered [GET] - View all registered events sorted by event chronologically
    /admin/events/{event_id} [PUT] - Update an event
    /admin/events/{event_id}/summary [GET] - View a summary of an event

'''
urlpatterns = [
    path("events/", EventListView.as_view(), name="event_list"),
    path("events/<int:event_id>/book/", BookEventTicket.as_view(), name="event_book"),
    path("events/<int:event_id>/ticket/<int:ticket_id>/", BookTicketView.as_view(), name="view_book_ticket"),
    path("events/registered/", RegisteredEventsList.as_view(), name="registered_event"),
    path("events/create/", EventCreateAdmin.as_view(), name="create_event"),
    path("events/update/<int:event_id>/", EventUpdateAdmin.as_view(), name="event_update"),
    path("events/<int:id>/summary/", EventSummaryAdmin.as_view(), name="event_summary"),

]
