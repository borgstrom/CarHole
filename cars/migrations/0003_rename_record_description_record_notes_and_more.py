# Generated by Django 4.2.4 on 2023-08-20 20:27

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_record_cost_record_cost_currency_record_odometer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="description",
            new_name="notes",
        ),
        migrations.AlterField(
            model_name="record",
            name="cost_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("USD", "US Dollar")],
                default="USD",
                editable=False,
                max_length=3,
                null=True,
            ),
        ),
    ]