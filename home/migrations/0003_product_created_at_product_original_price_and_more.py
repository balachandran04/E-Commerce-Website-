# Generated by Django 4.2.5 on 2023-09-07 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_image_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(default=0.0, max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-Hidden'),
        ),
        migrations.AddField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default,1-Trending'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category_images/default.jpg', upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500),
        ),

        # ...
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),  # Make sure this line exists
        ),
        # ...
    ]

