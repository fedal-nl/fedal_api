# Generated by Django 4.0.4 on 2023-08-22 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spanglish', '0009_remove_translation_word_or_sentence_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='translation',
            name='word_or_sentence',
        ),
    ]
