from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Event, Ticket
from .serializers import EventSerializer, TicketSerializer


class EventTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(
            username='admin', email='admin@example.com', password='testpass123', is_admin=True)
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass123')
        self.event1 = Event.objects.create(
            name='Test Event 1',
            description='Test event description',
            start_time=datetime.now() + timedelta(days=1),
            end_time=datetime.now() + timedelta(days=2),
            is_online=True,
            max_seats=100,
            booking_open_window_start=datetime.now() - timedelta(days=1),
            booking_open_window_end=datetime.now() + timedelta(days=1)
        )
        self.event2 = Event.objects.create(
            name='Test Event 2',
            description='Test event description',
            start_time=datetime.now() + timedelta(days=3),
            end_time=datetime.now() + timedelta(days=4),
            is_online=False,
            max_seats=50,
            booking_open_window_start=datetime.now() - timedelta(days=3),
            booking_open_window_end=datetime.now() + timedelta(days=3)
        )
        self.ticket1 = Ticket.objects.create(
            user=self.user,
            event=self.event1,
            ticket_code='testcode123'
        )
        self.ticket2 = Ticket.objects.create(
            user=self.user,
            event=self.event2,
            ticket_code='testcode456'
        )

    def test_get_all_events(self):
        response = self.client.get(reverse('event-list'))
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_event(self):
        response = self.client.get(
            reverse('event-detail', kwargs={'pk': self.event1.id}))
        event = Event.objects.get(id=self.event1.id)
        serializer = EventSerializer(event)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_ticket(self):
        data = {
            'user': self.user.id,
            'event': self.event2.id,
            'ticket_code': 'newtestcode123'
        }
        response = self.client.post(reverse('event-book', kwargs={'pk': self.event2.id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_ticket(self):
        response = self.client.get(reverse('ticket-detail', kwargs={'pk': self.ticket1.id}))
        ticket = Ticket.objects.get(id=self.ticket1.id)
        serializer = TicketSerializer(ticket)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_registered_events(self):
        response = self.client.get(reverse('event-registered'))
        events = Event.objects.filter(tickets__user=self.user).order_by('start_time')
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        data = {
            'name': 'New Test Event',
            'description': '
