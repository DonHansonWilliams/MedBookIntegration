from django.db import models


# Create your models here.

class Scheme(models.Model):
    corp_id = models.CharField(primary_key=True, null=False, max_length=100)
    scheme_code = models.CharField(null=False, max_length=100)
    scheme_name = models.CharField(null=False, max_length=200)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    renewal_date = models.DateField(null=False)
    anniv = models.IntegerField(null=False)

    class Meta:
        managed = False
        app_label = 'schemes'
        db_table = "mb_schemes"


class SchemeGroups(models.Model):
    idx = models.IntegerField(primary_key=True)
    category = models.CharField(null=False, max_length=50)
    benefit = models.CharField(null=False, max_length=100)
    ben_code = models.IntegerField(null=False)
    ben_limit = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    anniv = models.IntegerField(null=False)
    ben_share = models.CharField(null=False, max_length=100)
    corp_id = models.CharField(null=False, max_length=30)

    class Meta:
        app_label = 'schemes'
        db_table = "mb_scheme_groups"
