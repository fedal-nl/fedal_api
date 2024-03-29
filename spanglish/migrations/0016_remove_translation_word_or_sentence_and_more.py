# Generated by Django 4.0.4 on 2023-08-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spanglish', '0015_remove_translation_word_or_sentence_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='translation',
            name='word_or_sentence',
        ),
        migrations.AddConstraint(
            model_name='translation',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('sentence__isnull', False), ('word__isnull', True)), models.Q(('sentence__isnull', True), ('word__isnull', False)), _connector='OR'), name='word or sentence can not both be null or both be not null'),
        ),
    ]
