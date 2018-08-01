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
                ('scheme_code', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('scheme_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'medbook_scheme',
            },
        ),
    ]
