# Generated by Django 2.2 on 2021-01-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('street_1', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=200)),
                ('country_iso2', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'billing_address',
            },
        ),
    ]