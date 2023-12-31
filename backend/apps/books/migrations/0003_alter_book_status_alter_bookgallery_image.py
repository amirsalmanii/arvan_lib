# Generated by Django 4.2.6 on 2023-11-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_bookgallery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.CharField(
                choices=[
                    ("d", "Deleted"),
                    ("b", "Borrowed"),
                    ("a", "Available"),
                    ("u", "UnAvailable"),
                ],
                default="a",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="bookgallery",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
