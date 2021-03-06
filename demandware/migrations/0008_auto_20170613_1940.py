# Generated by Django 2.0.dev20170604010711 on 2017-06-13 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demandware', '0007_auto_20170613_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Category_CategoryParent', to='demandware.Category'),
        ),
        migrations.AlterField(
            model_name='categorymeta',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CategoryMeta_Category', to='demandware.Category'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProductCategory_Category', to='demandware.Category'),
        ),
    ]
