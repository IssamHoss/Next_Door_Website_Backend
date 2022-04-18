from asyncio.format_helpers import extract_stack
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style= {'input_type': 'password'}, write_only= True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'name', 'neighbourhood' ,'password' , 'password2']
        extract_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            name = self.validated_data['name'],
            neighbourhood = self.validated_data['neighbourhood'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        
        account.set_password(password)
        account.save()
        return account

