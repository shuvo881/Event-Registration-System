from rest_framework.response import Response
from rest_framework import viewsets, status
from events.models import Event, Registration
from events.serializers import EventSerializer, RegistrationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get_queryset(self):
        queryset = Event.objects.all()
        search_query = self.request.query_params.get('search_query', None)

        if search_query:
            queryset = Event.search_events(search_query)

        return queryset

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        event_id = request.data.get('event')
        event = Event.objects.get(id=event_id)

        if event.available_slots > 0:
            event.available_slots -= 1
            event.save()
            registration = Registration.objects.create(user=request.user, event=event)
            serializer = RegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'No available slots'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        regi_id = kwargs['pk']
        regi = Registration.objects.filter(id=regi_id).first()
        event = Event.objects.get(id=regi.event.pk)
        if event:
            event.available_slots += 1
            event.save()
        return super().destroy(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Registration.objects.all()
        userID = self.request.query_params.get('userID', None)

        if userID:
            queryset = queryset.filter(user=userID)

        return queryset
