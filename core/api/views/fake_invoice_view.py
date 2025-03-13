from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.services.fake_invoice_service import FakeInvoiceService
from core.domain.models.fake_invoice import FakeInvoice
from core.domain.serializers.fake_invoice_serializer import FakeInvoiceSerializer

class FakeInvoiceViewSet(viewsets.ViewSet):
    serializer_class = FakeInvoiceSerializer

    def list(self, request):
        invoices = FakeInvoiceService.get_all_invoices()
        serializer = self.serializer_class(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            invoice = FakeInvoiceService.get_invoice_by_id(pk)
            serializer = self.serializer_class(invoice)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FakeInvoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            sale_id = request.data.get("sale_id")
            invoice = FakeInvoiceService.generate_invoice(sale_id)
            serializer = self.serializer_class(invoice)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        try:
            invoice = FakeInvoice.objects.get(id=pk)
            return FileResponse(open(invoice.pdf_file.path, "rb"), as_attachment=True, filename=f"nota_fiscal_{invoice.id}.pdf")
        except FakeInvoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
