from heart.models.department import Department
from django_filters import CharFilter, FilterSet

class DepartmentFilter(FilterSet):

    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model= Department
        fields = ('id','name', 'date_added', 'deleted')