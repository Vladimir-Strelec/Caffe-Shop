# Generated by Django 4.0.3 on 2022-04-06 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_commentsproducts_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.abstractproduct'),
        ),
    ]
