# Generated by Django 2.2.6 on 2019-10-19 16:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.State'),
        ),
        migrations.AlterField(
            model_name='address',
            name='suburb',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
