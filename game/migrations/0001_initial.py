# Generated by Django 2.2.5 on 2019-11-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='post image')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
    ]
