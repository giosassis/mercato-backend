from rest_framework import status, viewsets
from rest_framework.response import Response
from core.services.sale_service import SaleService
from core.domain.serializers.sale_serializer import SaleSerializer


class SaleViewSet(viewsets.ViewSet):
    serializer_class = SaleSerializer

    def list(self, request):
        sales = SaleService.get_all_sales()
        serializer = self.serializer_class(sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = SaleSerializer(data=request.data)
            if serializer.is_valid():
                sale = SaleService.create_sale(serializer.validated_data)
                return Response(
                    SaleSerializer(sale).data, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            sale = SaleService.get_sale_by_id(pk)
            serializer = self.serializer_class(sale)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            SaleService.delete_sale(pk)
            return Response(
                {"message": "Sale successfully deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
