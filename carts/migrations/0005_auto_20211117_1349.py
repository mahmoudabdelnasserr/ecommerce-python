# Generated by Django 3.2.9 on 2021-11-17 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productgallery'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0004_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wishlist_id',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.wishlist')),
            ],
        ),
    ]
