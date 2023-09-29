# Generated by Django 4.2.4 on 2023-09-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBibCircular', '0012_alter_comentario_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='lugar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
    ]