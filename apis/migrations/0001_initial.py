# Generated by Django 3.2 on 2021-06-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.TextField(max_length=3000)),
                ('project_deadline', models.TextField(max_length=3000)),
                ('project_image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.IntegerField()),
                ('Task_name', models.TextField(max_length=3000)),
                ('Task_details', models.TextField(max_length=3000)),
            ],
        ),
    ]