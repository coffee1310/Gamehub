# Generated by Django 4.2.4 on 2023-09-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.product')),
                ('size', models.CharField(choices=[('Big', 'Большой'), ('Middle', 'Средний'), ('Small', 'Маленький')], default='Middle', max_length=10)),
                ('DPI', models.CharField(choices=[('less than 5000', 'Менее 5000'), ('5001-10000', '5000-10000'), ('10001-15000', '10001-15000'), ('15001-20000', '15001-20000')], default='5000-10000', max_length=20)),
                ('case_color', models.CharField(choices=[('Beige', 'Бежевый'), ('White', 'Белый'), ('Turquoise', 'Бирюзовый'), ('Blue', 'Синий'), ('Yellow', 'Желтый'), ('Black', 'Черный')], default='Black', max_length=10)),
                ('sensor_type', models.CharField(choices=[('Laser', 'Лазерный'), ('Optical LED', 'Оптический светодиодный')], default='Laser', max_length=20)),
            ],
            bases=('app.product',),
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='product_comments', to='app.comments'),
        ),
    ]
