# Generated by Django 3.2.20 on 2023-09-25 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0011_expense_expense_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='hsn',
        ),
    ]
