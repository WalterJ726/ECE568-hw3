# Generated by Django 4.0.8 on 2023-02-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
