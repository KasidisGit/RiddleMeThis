# Generated by Django 2.2.5 on 2019-11-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20191124_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='easyquestion',
            name='is_pass',
            field=models.BooleanField(),
        ),
    ]
