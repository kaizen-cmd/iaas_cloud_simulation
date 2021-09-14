# Generated by Django 3.2.7 on 2021-09-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_container_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(default=5000)),
            ],
        ),
        migrations.RemoveField(
            model_name='container',
            name='port',
        ),
    ]