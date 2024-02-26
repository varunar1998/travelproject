# Generated by Django 5.0.2 on 2024-02-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='desc',
            field=models.TextField(),
        ),
    ]