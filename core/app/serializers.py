from rest_framework import serializers

from .models import ToDO

class ToDoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDO
        fields = ('title', 'description')

class ToDoListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDO
        fields = ('id', 'title', 'created_date')

class ToDoDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDO
        fields = '__all__'        
        