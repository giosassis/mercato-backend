from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from core.services.product_service import ProductService
from core.domain.serializers.product_serializer import ProductSerializer
from core.permissions import IsManager
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsManager]
    queryset = ProductService.get_all_products()
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return ProductService.get_product_by_id(pk)
        except ValueError:
            raise NotFound("Product not found")
        
    def list_by_category(self, request, category_id=None):
        try:
            products = ProductService.get_products_by_category(category_id)
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        product = self.get_object(pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            product = ProductService.create_product(serializer.validated_data)
        except ValueError as e:
            raise ValidationError(str(e))

        return Response(self.get_serializer(product).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_product = ProductService.update_product(pk, serializer.validated_data)
        return Response(self.get_serializer(updated_product).data, status=status.HTTP_200_OK)
