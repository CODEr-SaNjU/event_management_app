from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .serializers import  EventSerializer, TicketSerializer, EventCreateUpdateSerializer, BookTicketViewSerializer
from rest_framework.response import Response
from .models import Event, Ticket
from django.db.models import Sum

# User Views
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('booking_open_window_start')
    serializer_class = EventSerializer


class BookTicketView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookTicketViewSerializer

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        ticket_id = self.kwargs.get('ticket_id')
        queryset = Ticket.objects.filter(event_id=event_id).filter(id=ticket_id)
        return queryset

# Admin Views

class EventCreateAdmin(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = EventCreateUpdateSerializer


class EventUpdateAdmin(generics.UpdateAPIView):
    lookup_url_kwarg = 'event_id'
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer


class EventSummaryAdmin(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)
        booked_ticket = Ticket.objects.filter(event_id = serializer.data['id']).aggregate(Sum('quantity'))
        summary = {
            'event_name': serializer.data['name'],
            'total_tickets': serializer.data['max_seats'],
            'total_earning_from_tickets': booked_ticket['quantity__sum'] * serializer.data['price'],
            'tickets_booked': booked_ticket['quantity__sum'],
            'available_tickets': serializer.data['max_seats']-booked_ticket['quantity__sum']
        }
        # serializer_data = serializer.data
        # serializer_data.update(summary)
        return Response(summary)


#user views
class BookEventTicket(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookEventTicket(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketSerializer
    
    def get_event(self):
        event_id = self.kwargs.get('event_id')
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise NotFound('Event not found')
        return event

    def perform_create(self, serializer):
        event = self.get_event()
        event_id = self.kwargs.get('event_id')
        tickets = Ticket.objects.filter(event_id = event_id).aggregate(Sum('quantity'))
        if not event.is_event_ticket_availabe:
            raise NotFound('Event not found')
        if timezone.now() < event.booking_open_window_start:
            raise NotFound("Booking is not opend yet")
        
        if timezone.now() > event.booking_open_window_end:
            raise NotFound('Booking is closed')
            
        if  tickets['quantity__sum'] >= event.max_seats:
            raise NotFound('No seats available')
        serializer.save(user=self.request.user, event=event)



class RegisteredEventsList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(event_date__gte=timezone.localtime()).order_by('event_date')