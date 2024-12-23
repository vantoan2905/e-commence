# Generated by Django 5.1.4 on 2024-12-23 07:21

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to=""
                    ),
                ),
                ("price", models.FloatField()),
                (
                    "articleNumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "articleType",
                    models.CharField(default="Unspecified", max_length=255),
                ),
                (
                    "productDisplayName",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "masterCategory",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "subCategory",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("gender", models.CharField(blank=True, max_length=255, null=True)),
                ("baseColour", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "fashionType",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("season", models.CharField(blank=True, max_length=255, null=True)),
                ("year", models.CharField(blank=True, max_length=255, null=True)),
                ("usag", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ClickHistory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("click_date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="click_histories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="click_histories",
                        to="shop.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
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
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                (
                    "rating_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="shop.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchHistory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("query", models.CharField(default=None, max_length=255)),
                (
                    "search_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="search_histories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewHistory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("view_date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="view_histories",
                        to="shop.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="view_histories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
