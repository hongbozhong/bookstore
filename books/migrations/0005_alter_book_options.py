# Generated by Django 4.0.1 on 2022-01-26 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('speical_status', 'can read all books')]},
        ),
    ]
