from django.http import Http404

# REST_FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
from rest_framework import status, generics
from rest_framework.permissions import (
    IsAuthenticated
)

from core.models import (
    Recipe,
    Tag,
    Ingredient
)

from .serializer import (
    RecipeListSerializer,
    RecipeDetailSerializer,
    TagSerializer,
    IngredientSerializer,
    RecipeImageSerializer
)

from .permissions import (
    IsOwnerOrReadOnly
)


# Create your views here.

# class RecipeListAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         recipes = Recipe.objects.order_by('-id')
#         serializer = RecipeListSerializer(recipes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class RecipeListAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = RecipeListSerializer

    def get_queryset(self):
        queryset = Recipe.objects.order_by('-id')
        tags = self.request.query_params.get('tags')
        ingredients = self.request.query_params.get('ingredients')

        if tags:
            tags_list = [int(i) for i in tags.split(',')]
            return queryset.filter(tags__in=tags_list)

        if ingredients:
            ingredients_list = [int(i) for i in ingredients.split(',')]
            return queryset.filter(ingredients__in=ingredients_list)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailAPI(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeDetailSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serilizer = RecipeDetailSerializer(recipe, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(
                serilizer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serilizer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk):
        recipe = self.get_object(pk)
        serilizer = RecipeDetailSerializer(
            recipe,
            data=request.data,
            partial=True
        )
        if serilizer.is_valid():
            serilizer.save()
            return Response(
                serilizer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serilizer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response({
            'info': 'recipe deleted'
            },
            status=status.HTTP_204_NO_CONTENT
        )


class TagListAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.order_by('-id')


class TagDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = TagSerializer
    queryset = Tag.objects.order_by('-id')


class IngredientListAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.order_by('-id')


class IngredientDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.order_by('-id')


class RecipeImageUploadView(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    queryset = Recipe.objects.all()
    serializer_class = RecipeImageSerializer
