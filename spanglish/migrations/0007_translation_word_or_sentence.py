# Generated by Django 4.0.4 on 2023-08-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spanglish', '0006_alter_translation_language_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='translation',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('sentence__isnull', False), ('word__isnull', False)), models.Q(('sentence__isnull', True), ('word__isnull', True)), _connector='OR'), name='word_or_sentence'),
        ),
    ]
