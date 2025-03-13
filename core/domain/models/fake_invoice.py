import uuid
import random
from django.db import models
from core.domain.models.sale import Sale

class FakeInvoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, related_name="invoice")
    issue_date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=255, default="Mercato Supermercado")
    company_cnpj = models.CharField(max_length=18, default="01.257.358/0001-67")
    client_name = models.CharField(max_length=255, default="Consumidor Final")
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to="invoices/", null=True, blank=True)
    access_key = models.CharField(max_length=44, unique=True, blank=True)
    protocol = models.CharField(max_length=16, unique=True, blank=True)
    invoice_number = models.CharField(max_length=9, unique=True, blank=True)
    company_legal_name = models.CharField(max_length=255, default="Mercato Software e Mercados LTDA")
    company_state_registration = models.CharField(max_length=20, default="987654321")
    company_address = models.CharField(max_length=255, default="Rua Líbero Badaró, Taquara, Rio de Janeiro - CEP: 22713-110")
    company_phone = models.CharField(max_length=20, default="(21) 12345-6789")
    company_email = models.EmailField(default="contato@mercato.com.br")

    def save(self, *args, **kwargs):
        if not self.access_key:
            self.access_key = self.generate_access_key()
        if not self.protocol:
            self.protocol = self.generate_protocol()
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_access_key():
        return ''.join(str(random.randint(0, 9)) for _ in range(44))

    @staticmethod
    def generate_protocol():
        return ''.join(str(random.randint(0, 9)) for _ in range(16))

    @staticmethod
    def generate_invoice_number():
        return ''.join(str(random.randint(0, 9)) for _ in range(9))

    def __str__(self):
        return f"FakeInvoice {self.invoice_number} - {self.client_name} - R$ {self.total_value}"
