# Generated by Django 2.2.6 on 2019-10-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191019_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='contact_name',
        ),
        migrations.AddField(
            model_name='address',
            name='contact_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='suburb',
            field=models.CharField(db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]