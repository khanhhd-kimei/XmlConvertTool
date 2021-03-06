# Generated by Django 2.0.dev20170604010711 on 2017-06-13 05:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(default='', max_length=100, unique=True)),
                ('category_name', models.CharField(default='', max_length=100)),
                ('category_name_jp', models.CharField(max_length=100, null=True)),
                ('category_name_cn', models.CharField(max_length=100, null=True)),
                ('category_name_fr', models.CharField(max_length=100, null=True)),
                ('category_parent', models.CharField(default='', max_length=100)),
                ('category_level', models.IntegerField(default=0)),
                ('del_flg', models.BooleanField(default=False)),
                ('create_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'dtb_categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=100)),
                ('value', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CategoryMeta_Category', to='demandware.Category', to_field='category_id')),
            ],
            options={
                'db_table': 'dtb_category_metadata',
            },
        ),
        migrations.CreateModel(
            name='HeaderMgr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_type', models.SmallIntegerField(choices=[(1, 'Product'), (2, 'Category')], db_index=True, default=1)),
                ('header_name', models.CharField(default='', max_length=50)),
                ('del_flg', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'dtb_header_mgr',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProductCategory_Category', to='demandware.Category', to_field='category_id')),
            ],
            options={
                'db_table': 'dtb_product_category',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_code', models.CharField(default='', max_length=10)),
                ('image_size', models.CharField(default='', max_length=10)),
                ('product_image', models.CharField(default='', max_length=255)),
                ('product_image_description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'dtb_product_image',
            },
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='', max_length=100, unique=True)),
                ('season_code', models.CharField(default='', max_length=100)),
                ('season_display_name', models.CharField(default='', max_length=100)),
                ('brand_code', models.CharField(default='', max_length=100)),
                ('brand_display_name', models.CharField(default='', max_length=100)),
                ('display_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('functions', models.TextField(default='')),
                ('online_shop_url', models.CharField(default='', max_length=255)),
                ('product_commentary_1_image', models.CharField(default='', max_length=255)),
                ('product_commentary_1_description', models.TextField(null=True)),
                ('product_commentary_2_image', models.CharField(default='', max_length=255)),
                ('product_commentary_2_description', models.TextField(null=True)),
                ('product_commentary_3_image', models.CharField(default='', max_length=255)),
                ('product_commentary_3_description', models.TextField(null=True)),
                ('product_commentary_image_title', models.CharField(max_length=255, null=True)),
                ('main_image', models.CharField(default='', max_length=255)),
                ('del_flg', models.BooleanField(default=False)),
                ('create_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'dtb_product_master',
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=100)),
                ('value', models.TextField(null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProductMeta_ProductMaster', to='demandware.ProductMaster', to_field='product_id')),
            ],
            options={
                'db_table': 'dtb_product_metadata',
            },
        ),
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='RelatedProduct_product_id', to='demandware.ProductMaster', to_field='product_id')),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='RelatedProduct_related_product_id', to='demandware.ProductMaster', to_field='product_id')),
            ],
            options={
                'db_table': 'dtb_related_product',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_jan', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=50)),
                ('size_code', models.CharField(default='', max_length=10)),
                ('size_display_name', models.CharField(default='', max_length=100)),
                ('color_code', models.CharField(default='', max_length=10)),
                ('color_display_name', models.CharField(default='', max_length=100)),
                ('color_hexa_code', models.CharField(default='', max_length=10)),
                ('price_amount', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('stock_quantity', models.IntegerField(default=1)),
                ('del_flg', models.BooleanField(default=False)),
                ('create_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Variant_ProductMaster', to='demandware.ProductMaster', to_field='product_id')),
            ],
            options={
                'db_table': 'dtb_variant',
            },
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProductImage_ProductMaster', to='demandware.ProductMaster', to_field='product_id'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProductCategory_ProductMaster', to='demandware.ProductMaster', to_field='product_id'),
        ),
        migrations.AlterUniqueTogether(
            name='productmeta',
            unique_together={('product_id', 'key')},
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('product_id', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='categorymeta',
            unique_together={('category', 'key')},
        ),
    ]
