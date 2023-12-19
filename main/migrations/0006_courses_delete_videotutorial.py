# Generated by Django 5.0 on 2023-12-19 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('format', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('age', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='VideoTutorial',
        ),
    ]
