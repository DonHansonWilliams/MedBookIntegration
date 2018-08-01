from django.db import models


# Create your models here.

class Scheme(models.Model):
    scheme_code = models.CharField(primary_key=True, null=False, max_length=100)
    scheme_name = models.CharField(null=False, max_length=200)

    class Meta:
        app_label = 'schemes'
        db_table = "scheme"