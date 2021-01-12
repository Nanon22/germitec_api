from rest_framework import viewsets
from heart.api.filters.department import DepartmentFilter
from heart.api.serializers.department import DepartmentSerializer
from heart.models.department import Department
from rest_framework.permissions import IsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.order_by('pk')
    serializer_class = DepartmentSerializer
    filter_class = DepartmentFilter