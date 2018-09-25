# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('scheme_code', models.CharField(primary_key=True, max_length=100, serialize=False)),
                ('scheme_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'schemes',
                'managed': False,
            },
        ),
    ]
