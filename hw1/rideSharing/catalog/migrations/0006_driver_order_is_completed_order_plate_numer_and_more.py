# Generated by Django 4.0.8 on 2023-02-12 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_order_completed_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.user')),
                ('vehicle_type', models.CharField(choices=[('b', 'BMW'), ('f', 'Ford'), ('k', 'Kia'), ('m', 'Maserati'), ('n', 'Nissan')], max_length=1)),
                ('maxslot', models.SmallIntegerField()),
                ('plate_number', models.IntegerField()),
            ],
            bases=('catalog.user',),
        ),
        migrations.AddField(
            model_name='order',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='plate_numer',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='completed_time',
            field=models.DateTimeField(default='2023-2-11 15:30:30'),
        ),
    ]