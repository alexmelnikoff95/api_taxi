# Generated by Django 4.2 on 2023-05-05 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_reviews', '0002_alter_review_parent_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api_reviews.product', verbose_name='Продукт'),
        ),
    ]
