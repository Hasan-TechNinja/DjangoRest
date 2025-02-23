# Generated by Django 5.1.6 on 2025-02-23 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('joinDate', models.DateField(auto_now_add=True)),
                ('leavingDate', models.DateField(blank=True, default=None)),
            ],
        ),
    ]
