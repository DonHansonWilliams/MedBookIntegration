# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('clm_ex_id', models.AutoField(max_length=100, serialize=False, primary_key=True)),
                ('member_no', models.CharField(max_length=20)),
                ('invoice_no', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=200, null=True)),
                ('provider', models.CharField(max_length=200, null=True)),
                ('claim_no', models.CharField(max_length=200, null=True)),
                ('invoice_date', models.DateField()),
                ('diagnosis', models.CharField(max_length=100, null=True)),
                ('anniv', models.IntegerField(null=True)),
                ('copay_amt', models.DecimalField(null=True, max_digits=15, decimal_places=2)),
                ('prov_code', models.IntegerField()),
                ('ben_code', models.IntegerField()),
                ('invoiced_amt', models.DecimalField(max_digits=15, decimal_places=2)),
                ('uploaded', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'claims',
            },
        ),
        migrations.AlterUniqueTogether(
            name='claim',
            unique_together=set([('invoice_no', 'service', 'prov_code')]),
        ),
    ]
