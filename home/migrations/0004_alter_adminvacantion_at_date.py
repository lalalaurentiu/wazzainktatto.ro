# Generated by Django 4.0 on 2022-01-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_adminvacantion_at_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminvacantion',
            name='at_date',
            field=models.DateField(),
        ),
    ]
