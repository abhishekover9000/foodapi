# Generated by Django 2.1.2 on 2018-11-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20181103_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='measurement',
            field=models.CharField(max_length=4),
        ),
    ]
