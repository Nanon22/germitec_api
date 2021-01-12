from rest_framework import serializers
from heart.models.department import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Department
        fields = ('id', 'url', 'name', 'date_added', 'deleted')
        extra_kwargs = {'date_added': {'read_only': True}}