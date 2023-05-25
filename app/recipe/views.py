from django.http import Http404

# REST_FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import (
    IsAuthenticated
)

from core.models import Recipe, Tag
from .serializer import (
    RecipeListSerializer,
    RecipeDetailSerializer,
    TagSerializer
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
    queryset = Recipe.objects.order_by('-id')

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
