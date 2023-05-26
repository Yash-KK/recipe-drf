from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient
)


class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'description', 'link',
            'tags', 'ingredients'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        ingredients_data = validated_data.pop('ingredients', [])

        user = self.context['request'].user
        recipe = super().create(validated_data)

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(user=user, **tag_data)
            recipe.tags.add(tag)

        for ingredient_data in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(
                user=user,
                **ingredient_data
            )
            recipe.ingredients.add(ingredient)

        return recipe

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
    tags = serializers.StringRelatedField(many=True, required=False)
    ingredients = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Recipe
        fields = RecipeListSerializer.Meta.fields + [
            'description',
            'tags',
            'ingredients',
            'image'
        ]
