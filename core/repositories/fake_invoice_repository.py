from core.domain.models.fake_invoice import FakeInvoice

class FakeInvoiceRepository:
    @staticmethod
    def get_all():
        return FakeInvoice.objects.all()

    @staticmethod
    def get_by_id(invoice_id):
        return FakeInvoice.objects.filter(id=invoice_id).first()

    @staticmethod
    def create(data):
        return FakeInvoice.objects.create(**data)

    @staticmethod
    def update(invoice, data):
        for key, value in data.items():
            setattr(invoice, key, value)
        invoice.save()
        return invoice

    @staticmethod
    def delete(invoice):
        invoice.delete()