from django.db import models


# Create your models here.
class Preauth(models.Model):
    pre_auth_no = models.AutoField(primary_key=True, null=False, max_length=100)
    member_no = models.CharField(null=False, max_length=20)
    date_requested = models.DateField(null=False)
    diagnosis = models.CharField(null=False, max_length=100)
    ben_code = models.IntegerField(null=False)
    prov_code = models.IntegerField(null=False)
    requested_amt = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    deducted_amt = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    deduction_reason = models.CharField(null=True, max_length=100)
    approved_amount = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    request_notes = models.CharField(null=True, max_length=200)
    requested_by = models.CharField(null=False, max_length=100)

    class Meta:
        app_label = 'preauth'
        db_table = "mb_pre_auth"
