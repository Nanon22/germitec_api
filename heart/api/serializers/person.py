from rest_framework import serializers
from heart.models.person import Person
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'last_name', 'first_name', 'email', 'is_staff')
        extra_kwargs = {'password': {'write_only': True, 'required': False}, 'username': {'required': False}}

class PersonSerializer(serializers.HyperlinkedModelSerializer):
     
    user = UserSerializer()
    
    class Meta:
        model = Person
        fields = ('id', 'url', 'user', 'department', 'status', 'date_added', 'deleted')
        extra_kwargs = {'date_added': {'read_only': True}}

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.create_user(**user_data)
        
        user.set_password(user_data['password'])

        person = Person.objects.create(user=user, **validated_data)
        return person

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        user = instance.user
        
        instance.department = validated_data.get('department', instance.department)
        instance.status = validated_data.get('status', instance.status)

        if 'username' in user_data:
            if user_data['username'] == user.username or user_data['username'].strip() == "" :
                pass
            else:
                user.username = user_data['username']
        
        user.last_name = user_data['last_name']
        user.first_name = user_data['first_name']
        user.email = user_data['email']
        user.is_staff = user_data['is_staff']

        if 'password' in user_data:
            if user_data['password'] is None:
                pass
            else:
                user.set_password(user_data['password'])

        instance.save()
        user.save()
        return instance