# Generated by Django 5.1.7 on 2025-03-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Criada"),
                    ("completed", "Comcluída"),
                    ("pending", "Pendente"),
                    ("refunded", "Reembolsada"),
                    ("canceled", "Cancelada"),
                ],
                default="created",
                max_length=10,
            ),
        ),
    ]
