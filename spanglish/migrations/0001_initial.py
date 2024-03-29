# Generated by Django 4.0.4 on 2023-08-21 23:59

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spanglish.category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spanglish.language')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, unique=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spanglish.category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spanglish.language')),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spanglish.language')),
                ('sentence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spanglish.sentence')),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spanglish.word')),
            ],
        ),
        migrations.AddIndex(
            model_name='word',
            index=models.Index(fields=['language', 'category'], name='spanglish_w_languag_3c910c_idx'),
        ),
        migrations.AddIndex(
            model_name='translation',
            index=models.Index(fields=['word', 'sentence'], name='spanglish_t_word_id_3799ae_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('sentence', 'language'), ('word', 'language')},
        ),
        migrations.AddIndex(
            model_name='sentence',
            index=models.Index(fields=['language', 'category'], name='spanglish_s_languag_e5e5c6_idx'),
        ),
    ]
