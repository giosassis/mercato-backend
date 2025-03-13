from django.template.loader import render_to_string
from django.utils.timezone import now
from weasyprint import HTML
import os

from core.domain.models.fake_invoice import FakeInvoice
from core.repositories.sale_repository import SaleRepository
from core.repositories.fake_invoice_repository import FakeInvoiceRepository

from django.core.exceptions import ObjectDoesNotExist

class FakeInvoiceService:
    @staticmethod
    def generate_invoice(sale_id):
        
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found.")

        invoice = FakeInvoiceRepository.create({
            "sale": sale,
            "client_name": sale.cashier.username,
            "total_value": sale.total
        })

        try:
            context = {"sale": sale, "invoice": invoice}
            html_string = render_to_string("fake_invoice.html", context)

            pdf_file_path = f"media/invoices/{invoice.id}.pdf"

            HTML(string=html_string).write_pdf(pdf_file_path)

            if not os.path.exists(pdf_file_path):
                raise ValueError("The PDF file was not created.")

            invoice.pdf_file = pdf_file_path
            FakeInvoiceRepository.update(invoice, {"pdf_file": pdf_file_path})

        except Exception as e:
            print(f"There was an error generating the PDF file: {e}")
            raise ValueError("There was an error generating the PDF file.")

        return invoice

    @staticmethod
    def get_all_invoices():
        return FakeInvoiceRepository.get_all()

    @staticmethod
    def get_invoice_by_id(invoice_id):
        return FakeInvoiceRepository.get_by_id(invoice_id)

    @staticmethod
    def delete_invoice(invoice_id):
        invoice = FakeInvoiceRepository.get_by_id(invoice_id)
        if invoice:
            FakeInvoiceRepository.delete(invoice)
        return invoice