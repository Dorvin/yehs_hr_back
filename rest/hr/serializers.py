from rest_framework import serializers
from .models import Event, Member

class EventBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'category', 'date')

class MemberSerializer(serializers.ModelSerializer):
    events = EventBasicSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = ('id', 'code', 'name', 'email', 'phone', 'yn', 'fn', 'univ', 'major', 'events')

class EventSerializer(serializers.ModelSerializer):
    participants = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'name', 'category', 'participants')