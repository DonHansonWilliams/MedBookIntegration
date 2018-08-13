# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverbenefits',
            name='rec_id',
            field=models.AutoField(default=1, max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='coverbenefits',
            name='benefits',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coverbenefits',
            name='family_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coverbenefits',
            name='member_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coverbenefits',
            name='scheme_code',
            field=models.CharField(max_length=10),
        ),
    ]
