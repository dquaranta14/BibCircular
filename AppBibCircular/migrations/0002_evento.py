# Generated by Django 4.2.4 on 2023-09-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBibCircular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
