# Generated by Django 4.0.5 on 2022-07-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_image_innercategory_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/categories/default.png', upload_to='images/categories'),
        ),
        migrations.AlterField(
            model_name='innercategory',
            name='image',
            field=models.ImageField(default='images/categories/default.png', upload_to='images/categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/products/default.png', upload_to='images/products'),
        ),
    ]
