# Generated by Django 3.2.24 on 2024-03-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0004_alter_score_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='nadimak',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]