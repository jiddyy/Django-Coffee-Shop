# Generated by Django 2.2.5 on 2019-11-07 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191107_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Coffee'),
        ),
    ]
