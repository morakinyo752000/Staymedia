# Generated by Django 4.2.3 on 2023-09-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(null=True)),
                ('file', models.ImageField(upload_to='blog_images')),
                ('created_at', models.DateTimeField(null=True)),
                ('min_read', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='')),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
    ]
