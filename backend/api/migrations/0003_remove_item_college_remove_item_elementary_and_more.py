# Generated by Django 5.0.6 on 2024-07-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_item_description_remove_item_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='college',
        ),
        migrations.RemoveField(
            model_name='item',
            name='elementary',
        ),
        migrations.RemoveField(
            model_name='item',
            name='secondary',
        ),
        migrations.AddField(
            model_name='item',
            name='pagibig_id_number',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='sss_number',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='tin_number',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
