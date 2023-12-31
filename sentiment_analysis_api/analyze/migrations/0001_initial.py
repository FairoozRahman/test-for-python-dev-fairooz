# Generated by Django 4.2.2 on 2023-06-24 20:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('text', models.TextField(blank=True, null=True)),
                ('result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Neutral', 'Neutral')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
