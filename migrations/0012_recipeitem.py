# Generated by Django 4.2 on 2023-04-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0011_fitnessblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=10)),
                ('image', models.ImageField(upload_to='portfolio_images/')),
                ('preview_link', models.URLField()),
                ('details_link', models.URLField()),
            ],
        ),
    ]
