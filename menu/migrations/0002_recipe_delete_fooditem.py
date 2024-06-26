# Generated by Django 4.2.8 on 2024-06-05 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="recipe/")),
                ("recipe_name", models.CharField(max_length=200)),
                ("ingredients", models.TextField()),
                ("instructions", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="menu.menu"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="FoodItem",
        ),
    ]
