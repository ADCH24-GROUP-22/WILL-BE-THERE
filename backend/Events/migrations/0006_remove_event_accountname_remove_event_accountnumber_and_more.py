# Generated by Django 5.0.7 on 2024-07-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_alter_event_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='accountName',
        ),
        migrations.RemoveField(
            model_name='event',
            name='accountNumber',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bankName',
        ),
        migrations.RemoveField(
            model_name='event',
            name='socialMedia',
        ),
        migrations.AddField(
            model_name='event',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='linkedIn',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
