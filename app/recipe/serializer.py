from rest_framework import serializers
from core.models import Recipe


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'description', 'link'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        if Recipe.objects.filter(title=data['title']).exists():
            raise serializers.ValidationError(
                "recipe with similar title already exist's"
            )
        return data

    def to_representation(self, instance):
        data = {
            'id': instance.id,
            'title': instance.title,
            'time_minutes': instance.time_minutes,
            'price': instance.price,
            'link': instance.link
        }
        return data


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = RecipeListSerializer.Meta.fields + ['description']
