# Generated by Django 4.2 on 2023-05-10 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0021_remove_recipeitem_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessblog',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
