# Generated by Django 5.0 on 2024-05-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]