# Generated by Django 3.2.4 on 2021-09-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0005_auto_20210901_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='occupation',
            field=models.TextField(default='Occupation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.TextField(),
        ),
    ]
