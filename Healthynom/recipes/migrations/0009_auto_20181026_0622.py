# Generated by Django 2.1.2 on 2018-10-26 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20181024_1351'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IngredientInRecipe',
            new_name='RecipeIngredient',
        ),
    ]