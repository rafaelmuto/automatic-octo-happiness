# Generated by Django 5.2.4 on 2025-07-18 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "library",
            "0004_author_created_at_author_updated_at_book_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="library.author",
            ),
        ),
    ]
