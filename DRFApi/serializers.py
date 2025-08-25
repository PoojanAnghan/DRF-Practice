from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50) 

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value <= 0:
            raise serializers.ValidationError("Roll number must be greater than 0")
        return value

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must only contain letters")
        return value
    
    def validate_city(self, value):
        if value is not str:
            raise serializers.ValidationError("Invalid city name")
        return value
    
    def validate(self, data):     # Data is the dictionary of the Field values
        name = data.get