# Generated by Django 4.0.4 on 2023-08-24 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spanglish', '0017_verbtense_alter_translation_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verb',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verb', to='spanglish.word'),
        ),
    ]
