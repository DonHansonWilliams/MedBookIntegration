from django.db import models


# Create your models here.

class Scheme(models.Model):
    scheme_code = models.CharField(primary_key=True, null=False)
    scheme_name = models.CharField(null=False)

    class Meta:
        app_label = 'schemes'
        db_table = "medbook_scheme"
