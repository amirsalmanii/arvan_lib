# Generated by Django 4.2.6 on 2023-11-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_alter_book_status_alter_bookgallery_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookgallery",
            name="image_url",
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
