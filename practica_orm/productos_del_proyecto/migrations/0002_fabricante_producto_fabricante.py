# Generated by Django 5.1.1 on 2024-10-13 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_del_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='fabricante',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.CASCADE, null=True, blank=True, to='productos_del_proyecto.fabricante'),
        ),
    ]
