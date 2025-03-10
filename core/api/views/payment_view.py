from rest_framework import status, viewsets
from rest_framework.response import Response
from core.services.payment_service import PaymentService
from core.domain.serializers.payment_serializer import PaymentSerializer


class PaymentViewSet(viewsets.ViewSet):
    serializer_class = PaymentSerializer

    def list(self, request, sale_id=None):
        try:
            payments = PaymentService.get_payments_by_sale(sale_id)
            serializer = self.serializer_class(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, sale_id=None):
        try:
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                payment = PaymentService.process_payment(
                    sale_id, serializer.validated_data
                )
                return Response(
                    PaymentSerializer(payment).data, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
