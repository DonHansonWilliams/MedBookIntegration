from django.db import models

# Create your models here.

class Scheme(models.Model):
    corp_id = models.CharField(primary_key=True, null=False, max_length=100)
    scheme_code = models.CharField(null=False, max_length=100)
    scheme_name = models.CharField(null=False, max_length=200)

    class Meta:
        managed = False
        app_label = 'schemes'
        db_table = "mb_schemes"
        