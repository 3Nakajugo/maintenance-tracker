# Generated by Django 2.1.7 on 2019-03-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintainance_requests', '0003_maintainancerequest_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintainancerequest',
            name='comment',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='maintainancerequest',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]