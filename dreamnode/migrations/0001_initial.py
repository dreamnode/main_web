# Generated by Django 3.1.7 on 2021-03-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='our_works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_images', models.ImageField(default='default.jpg', upload_to='pictures')),
                ('client', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('date', models.TextField()),
            ],
        ),
    ]
