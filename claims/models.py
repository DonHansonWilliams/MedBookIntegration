from django.db import models


# Create your models here.
class Claim(models.Model):
    clm_ex_id = models.AutoField(primary_key=True, null=False, max_length=100)
    member_no = models.CharField(null=False, max_length=20)
    invoice_no = models.CharField(null=False, max_length=100)
    service = models.CharField(null=True, max_length=200)
    provider = models.CharField(null=True, max_length=200)
    claim_no = models.CharField(null=True, max_length=200)
    invoice_date = models.DateField(null=False)
    diagnosis = models.CharField(null=True, max_length=100)
    anniv = models.IntegerField(null=True)
    copay_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    prov_code = models.IntegerField(null=False)
    ben_code = models.IntegerField(null=False)
    invoiced_amt = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    uploaded = models.IntegerField(null=True, default=0)

    class Meta:
        app_label = 'claims'
        db_table = "claims"
