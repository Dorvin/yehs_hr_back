from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event, Member
from .serializers import EventSerializer, EventBasicSerializer, MemberSerializer
import json

@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        if params.get('name', '') == '' or params.get('category', '') == '' or params.get('date', '') == '':
            content = {'warring': 'empty name or category or date is not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        event = Event(name=params.get('name', ''), category=params.get('category', ''), date=params.get('date', ''))
        event.save()
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'DELETE'])
def event_detail(request, pk):
    if request.method == 'GET':
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        event = Event.objects.get(pk=pk)
        if params.get('name', '') == '' or params.get('category', '') == '' or params.get('date', '') == '':
            content = {'warring': 'empty name or category or date is not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        event.name = params.get('name', '')
        event.category = params.get('category', '')
        event.date = params.get('date', '')
        event.save()
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        params = json.loads(request.body.decode("utf-8"))
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        member_infos = json.loads(request.body.decode("utf-8")).get('member_infos', [])
        if len(member_infos) == 0:
            content = {'warring': 'empty list of member_infos is not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        count = 0
        for member_info in member_infos:
            if member_info.get('code', '') == '' or member_info.get('name', '') == '':
                content = {'warring': 'empty code or name is not allowed'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            member = Member(code=member_info.get('code', ''), name=member_info.get('name', ''), \
                        email=member_info.get('email', ''), phone=member_info.get('phone', ''), \
                        yn=member_info.get('yn', ''), fn=member_info.get('fn', ''), \
                        univ=member_info.get('univ', ''), major=member_info.get('major', ''))
            member.save()
            count += 1
        content = {'success': f'{count} members have been successfully created'}
        return Response(content, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'DELETE'])
def member_detail(request, code):
    if request.method == 'GET':
        member = Member.objects.get(code=code)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        member = Member.objects.get(code=code)
        member.name = params.get('name', '')
        member.email = params.get('email', '')
        member.phone = params.get('phone', '')
        member.univ = params.get('univ', '')
        member.major = params.get('major', '')
        member.save()
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        member = Member.objects.get(code=code)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def event_register_member(request, pk):
    event = Event.objects.get(pk=pk)
    codes = json.loads(request.body.decode("utf-8")).get('codes', [])
    if len(codes) == 0:
        content = {'warring': 'empty list of codes is not allowed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    for code in codes:
        member = Member.objects.get(code=code)
        member.events.add(event)
        member.save()
    event.save()
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def success_member_list(request):
    params = json.loads(request.body.decode("utf-8"))
    members = Member.objects.all()
    success_members = []
    for member in members:
        events = member.events.all()
        condition = True
        # some logics about condtion here
        if condition:
            serializer = MemberSerializer(member)
            success_members.append(serializer.data)
    return Response(success_members)
