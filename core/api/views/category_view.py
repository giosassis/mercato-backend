from rest_framework import status, viewsets
from rest_framework.response import Response
from core.services.category_service import CategoryService
from core.domain.serializers.category_serializer import CategorySerializer

class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer  

    def list(self, request):
        categories = CategoryService.get_all_categories()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                category = CategoryService.create_category(serializer.validated_data)
                return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            category = CategoryService.get_category_by_id(pk)
            serializer = self.serializer_class(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            serializer = CategorySerializer(data=request.data, partial=True)
            if serializer.is_valid():
                updated_category = CategoryService.update_category(pk, serializer.validated_data)
                return Response(CategorySerializer(updated_category).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            CategoryService.delete_category(pk)
            return Response({"message": "Category was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
