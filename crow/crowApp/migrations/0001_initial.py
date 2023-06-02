# Generated by Django 4.2.1 on 2023-06-02 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrowPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', models.TextField()),
            ],
        ),
    ]
