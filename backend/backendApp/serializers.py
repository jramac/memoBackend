from rest_framework import serializers
from .models import Name,Score

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ['id', 'nadimak']

class ScoreSerializer(serializers.ModelSerializer):
    name = NameSerializer(required = True)
    class Meta:
        model = Score
        fields = ['id', 'name', 'score_value']

    def create(self, validated_data):
        name_data = validated_data.pop('name')
        name_instance, _ = Name.objects.get_or_create(**name_data)
        score_instance = Score.objects.create(name=name_instance, **validated_data)
        return score_instance