# Generated by Django 4.2 on 2023-05-13 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0028_remove_recipeitem_preview_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
