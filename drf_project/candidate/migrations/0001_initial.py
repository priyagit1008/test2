# Generated by Django 2.2.5 on 2019-11-09 16:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mycandidates',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('current_ctc', models.IntegerField()),
                ('expected_ctc', models.IntegerField()),
                ('notice_days', models.IntegerField()),
                ('is_alredy_on_notice', models.BooleanField()),
                ('tech_skills', models.CharField(max_length=20)),
                ('preferable_location', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
