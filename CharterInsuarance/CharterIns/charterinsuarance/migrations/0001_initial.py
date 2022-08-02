# Generated by Django 4.0.4 on 2022-06-30 09:04

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('displayname', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(default='N/A', max_length=200, null=True)),
                ('branchcode', models.CharField(max_length=10, null=True)),
                ('employeeID', models.CharField(max_length=20, unique=True)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_no', models.CharField(max_length=30)),
                ('amount', models.FloatField(max_length=30)),
                ('payermobile_no', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('txn_id', models.CharField(editable=False, max_length=30, null=True)),
                ('txn_date', models.DateTimeField(default=datetime.datetime(2022, 6, 30, 15, 4, 53, 930457), editable=False, null=True)),
                ('msg', models.CharField(default='S', editable=False, max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('input_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='charterinsuarance.user')),
            ],
        ),
    ]
