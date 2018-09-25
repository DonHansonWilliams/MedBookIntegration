# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverBenefits',
            fields=[
                ('scheme_code', models.CharField(max_length=20)),
                ('family_no', models.CharField(max_length=20)),
                ('member_no', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('benefit', models.CharField(primary_key=True, max_length=50)),
                ('benefit_code', models.IntegerField(null=True)),
                ('benefit_limit', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('waiting_period', models.IntegerField(null=True, default=0)),
                ('anniv', models.IntegerField(primary_key=True)),
                ('reserves', models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)),
                ('expenditure', models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)),
                ('balance', models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)),
            ],
            options={
                'db_table': 'coverBenefits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberDetails',
            fields=[
                ('scheme_code', models.CharField(max_length=20)),
                ('family_no', models.CharField(max_length=50)),
                ('member_no', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
                ('member_status', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mobile_no', models.CharField(max_length=15, null=True)),
                ('anniv', models.IntegerField()),
            ],
            options={
                'db_table': 'memberDetails',
                'managed': False,
            },
        ),
    ]
