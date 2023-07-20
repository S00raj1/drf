from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = '__all__'


    def validate(self, data):
        
        if data["age"] < 18:
            raise serializers.ValidationError({'error' : 'age cannot be less then 18'})
        
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error': 'name cannot be integer'})
        
        if data['phone']:
            if not data['phone'].isdigit():
                raise serializers.ValidationError({'error':'Phone number cannot be string'})
            if  len(data['phone'])<10:
                    raise serializers.ValidationError({'error': 'Phone number cannot be less then 10'})    
        
        return data

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'