# Generated by Django 3.0.2 on 2020-02-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
