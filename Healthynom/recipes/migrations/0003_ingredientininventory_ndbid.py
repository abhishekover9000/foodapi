# Generated by Django 2.1.2 on 2018-10-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20181024_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientininventory',
            name='ndbid',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
