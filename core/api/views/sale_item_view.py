from rest_framework import status, viewsets
from rest_framework.response import Response
from core.services.sale_item_service import SaleItemService
from core.serializers.sale_item_serializer import SaleItemSerializer


class SaleItemViewSet(viewsets.ViewSet):
    serializer_class = SaleItemSerializer

    def list(self, request, sale_id=None):
        try:
            sale_items = SaleItemService.get_items_by_sale(sale_id)
            serializer = self.serializer_class(sale_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, sale_id=None):
        try:
            serializer = SaleItemSerializer(data=request.data)
            if serializer.is_valid():
                sale_item = SaleItemService.add_item_to_sale(
                    sale_id, serializer.validated_data
                )
                return Response(
                    SaleItemSerializer(sale_item).data, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            SaleItemService.remove_item_from_sale(pk)
            return Response(
                {"message": "Item removed."}, status=status.HTTP_204_NO_CONTENT
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
