from rest_framework import serializers
from .models import CustomUser, Event, Ticket


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'is_active']
        read_only_fields = ['id', 'is_active']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        """
        Validate the input data for the event creation and update endpoints.
        """
        if not self.context['request'].user.is_superuser:
            raise serializers.ValidationError('You do not have permission to perform this action.')
        # Ensure that the start date is before the end date
        if data.get('start_date') and data.get('end_date'):
            if data['start_date'] >= data['end_date']:
                raise serializers.ValidationError('End date must be after start date')

        # Ensure that the booking open window is valid
        if data.get('booking_open_window'):
            booking_open_window = data['booking_open_window']
            if booking_open_window['start_time'] >= booking_open_window['end_time']:
                raise serializers.ValidationError('Booking open window end time must be after start time')
            if booking_open_window['start_time'] <= data['start_date']:
                raise serializers.ValidationError('Booking open window start time must be after event start date')
            if booking_open_window['end_time'] >= data['end_date']:
                raise serializers.ValidationError('Booking open window end time must be before event end date')

        return data

class TicketSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = Ticket
        fields = ('id', 'user', 'event', 'timestamp', 'quantity', 'total_price')


class BookTicketViewSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    user = CustomUserSerializer()
    event = EventSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'user', 'event', 'timestamp', 'quantity', 'total_price')
