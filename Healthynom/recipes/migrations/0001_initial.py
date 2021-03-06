# Generated by Django 2.1.2 on 2018-11-03 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ndbid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('measurement', models.FloatField(choices=[('lbs', 'pounds'), ('oz', 'ounces'), ('floz', 'fluid ounces'), ('g', 'grams')], max_length=4)),
                ('amount', models.PositiveIntegerField()),
                ('ingredient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('steps', models.TextField()),
                ('portions', models.PositiveSmallIntegerField()),
                ('people', models.PositiveSmallIntegerField()),
                ('prepTime', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=100)),
                ('ndbid', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('measurement', models.CharField(choices=[('lbs', 'pounds'), ('oz', 'ounces'), ('floz', 'fluid ounces'), ('g', 'grams')], max_length=4)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplied_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Supplier'),
        ),
    ]
