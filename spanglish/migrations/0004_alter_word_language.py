# Generated by Django 4.0.4 on 2023-08-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spanglish', '0003_alter_sentence_language_alter_word_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='spanglish.language'),
        ),
    ]
