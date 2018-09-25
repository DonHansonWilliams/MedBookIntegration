# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preauth',
            fields=[
                ('preauth_id', models.AutoField(primary_key=True, max_length=100, serialize=False)),
                ('member_no', models.CharField(max_length=20)),
                ('date_requested', models.DateField()),
                ('diagnosis', models.CharField(max_length=100)),
                ('ben_code', models.IntegerField()),
                ('prov_code', models.IntegerField()),
                ('requested_amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('deducted_amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('deduction_reason', models.CharField(max_length=100, null=True)),
                ('approved_amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('request_notes', models.CharField(max_length=200, null=True)),
                ('requested_by', models.CharField(max_length=100)),
                ('received', models.IntegerField(null=True, default=0)),
                ('approved', models.IntegerField(null=True, default=0)),
                ('uploaded', models.IntegerField(null=True, default=0)),
            ],
            options={
                'db_table': 'preauth',
            },
        ),
    ]
