from rest_framework import serializers
from .models import Name,Score

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'
    
class ScoreSerializer(serializers.ModelSerializer):
    name = NameSerializer(required = True)
    class Meta:
        model = Score
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name')
        name, created = Name.objects.get_or_create(**name_data)
        score = Score.objects.create(name = name,**validated_data)
        return score
    def update(self, instance, validated_data):
        name_data = validated_data.pop('name')

        # Retrieve the associated Name instance
        name_instance = instance.name
        print(name_instance)
        # Update the Name instance
        for key, value in name_data.items():
            setattr(name_instance, key, value)
        name_instance.save()

        # Update the Score instance
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
        
