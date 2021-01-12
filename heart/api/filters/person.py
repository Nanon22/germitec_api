from heart.models.person import Person
from django.contrib.auth.models import User
from django_filters import CharFilter, FilterSet

class PersonFilter(FilterSet):
    status = CharFilter(lookup_expr='icontains')

    class Meta:
        model= Person
        fields = ('id','user', 'status',  'date_added', 'deleted')