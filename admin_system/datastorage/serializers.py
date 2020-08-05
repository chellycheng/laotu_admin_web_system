from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_datetime', 'title', 'location', 'availability', 'speaker', 'discount_policy', 'description_picture', 'price_final']


