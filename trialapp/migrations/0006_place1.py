# Generated by Django 5.0.2 on 2024-02-20 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0005_delete_place1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pics')),
                ('desc1', models.TextField()),
            ],
        ),
    ]