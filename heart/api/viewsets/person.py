from rest_framework import viewsets
from heart.api.filters.person import PersonFilter
from heart.api.serializers.person import PersonSerializer
from heart.models.person import Person
from rest_framework.permissions import IsAuthenticated

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.order_by('pk')
    serializer_class = PersonSerializer
    filter_class = PersonFilter