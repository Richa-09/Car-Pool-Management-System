# Generated by Django 3.0.4 on 2020-03-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='time',
        ),
        migrations.AddField(
            model_name='offer',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
