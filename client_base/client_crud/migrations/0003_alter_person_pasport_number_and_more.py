# Generated by Django 5.1 on 2024-08-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_crud', '0002_person_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pasport_number',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='person',
            name='pasport_seria',
            field=models.CharField(max_length=4),
        ),
    ]
