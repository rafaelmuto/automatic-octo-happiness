# Generated by Django 5.2.4 on 2025-07-16 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_remove_author_nationality_author_country_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="open_library_key",
            new_name="olid",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="open_library_key",
            new_name="olid",
        ),
    ]
