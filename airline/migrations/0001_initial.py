# Generated by Django 4.2.1 on 2023-06-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airplane",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("passengers", models.IntegerField()),
            ],
        ),
    ]
