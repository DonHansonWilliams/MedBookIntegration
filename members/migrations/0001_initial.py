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
                ('rec_id', models.AutoField(default=1, max_length=100, serialize=False, primary_key=True)),
                ('benefits', models.CharField(max_length=50)),
                ('scheme_code', models.CharField(max_length=10)),
                ('family_no', models.CharField(max_length=50)),
                ('member_no', models.CharField(max_length=50)),
                ('benefit_limit', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('claims', models.DecimalField(default=0.0, null=True, max_digits=15, decimal_places=2)),
                ('reserve_amount', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('expense', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('benefit_status', models.CharField(max_length=20)),
                ('balance', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('waiting_period', models.IntegerField(null=True)),
                ('ben_code', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'cover_benefits',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_no', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('family_no', models.CharField(max_length=50)),
                ('scheme_code', models.CharField(max_length=10)),
                ('member_names', models.CharField(max_length=200)),
                ('member_status', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mobile_no', models.CharField(max_length=20, null=True)),
                ('anniv', models.IntegerField()),
            ],
            options={
                'db_table': 'member_details',
            },
        ),
    ]
