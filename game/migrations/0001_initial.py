# Generated by Django 2.2.5 on 2019-11-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EasyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/easy')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HardQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/hard')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MediumQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/medium')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
    ]