# Generated by Django 4.2.4 on 2023-09-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBibCircular', '0002_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='resena',
            field=models.TextField(null=True),
        ),
    ]
