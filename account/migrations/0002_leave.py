# Generated by Django 4.2 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=50)),
                ('leave_from', models.DateField()),
                ('leave_till', models.DateField()),
                ('reason', models.TextField()),
            ],
        ),
    ]
