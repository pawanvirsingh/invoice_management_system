# Generated by Django 3.0.10 on 2020-10-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='digitized',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_state',
            field=models.CharField(choices=[('processing', 'Processing'), ('digitized', 'Digitized'), ('failed', 'Failed')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
