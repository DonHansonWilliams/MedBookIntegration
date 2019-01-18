from django.db import models


# Create your models here.
class Claim(models.Model):
    clm_ex_id = models.AutoField(primary_key=True, null=False, max_length=100, auto_created=True)
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


class MedbookClaims(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    smart_provider = models.CharField(null=True, max_length=200)
    smart_trans_date = models.DateField(null=True)
    smart_service = models.CharField(null=True, max_length=3)
    smart_benefit = models.CharField(null=True, max_length=3)
    smart_bill_amount = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    uploaded = models.IntegerField(null=True, default=0)
    error = models.IntegerField(null=True, default=0)
    vetted = models.IntegerField(null=True, default=0)
    anniv = models.IntegerField(null=True)
    smart_member_no = models.CharField(null=True, max_length=20)
    smart_inv_no = models.CharField(null=True, max_length=100)
    pre_auth_no = models.IntegerField(null=True)
    fund = models.IntegerField(null=True)
    family_no = models.CharField(null=True, max_length=100)
    corp_id = models.CharField(null=True, max_length=100)
    smart_bill_id = models.CharField(null=True, max_length=50)
    claim_source = models.CharField(null=True, max_length=20)

    class Meta:
        app_label = 'claims'
        db_table = "smart_bills"


class ClaimStatus(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    invoice_no = models.CharField(null=False, max_length=50)
    bill_id = models.CharField(null=False, max_length=100)
    service = models.CharField(null=False, max_length=100)
    member_no = models.CharField(null=False, max_length=50)
    anniv = models.IntegerField(null=True)
    hospital = models.CharField(null=False, max_length=200)
    provider_code = models.IntegerField(null=False, default=0)
    vet_status = models.IntegerField(null=True, default=0)
    date_entered = models.DateField(null=True)
    invoiced_amount = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    deduction_amount = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    deduction_reason = models.CharField(null=True, max_length=100)
    amount_payable = models.DecimalField(null=True, max_digits=15, decimal_places=2)

    class Meta:
        app_label = 'claims'
        db_table = "mb_claim_status"


class Reimbursements(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    invoice_no = models.CharField(null=False, max_length=50)
    service = models.CharField(null=False, max_length=100)
    member_no = models.CharField(null=False, max_length=50)
    anniv = models.IntegerField(null=True)
    hospital = models.CharField(null=False, max_length=200)
    provider_code = models.IntegerField(null=False, default=0)
    date_entered = models.DateField(null=True)
    invoiced_amount = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    deduction_amount = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    deduction_reason = models.CharField(null=True, max_length=100)
    amount_payable = models.DecimalField(null=True, max_digits=15, decimal_places=2)

    class Meta:
        app_label = 'claims'
        db_table = "mb_reimbursements"


class ClaimsExperience(models.Model):
    idx = models.IntegerField(null=False, primary_key=True)
    corporate = models.CharField(null=False, max_length=200)
    principal_name = models.CharField(null=False, max_length=100)
    member_name = models.CharField(null=False, max_length=100)
    family_no = models.CharField(null=False, max_length=100)
    member_no = models.CharField(null=False, max_length=100)
    relation = models.CharField(null=False, max_length=100)
    anniv = models.IntegerField(null=False)
    claim_no = models.CharField(null=False, max_length=100)
    provider = models.CharField(null=False, max_length=200)
    invoice_no = models.CharField(null=False, max_length=100)
    service = models.CharField(null=False, max_length=100)
    invoice_date = models.DateField(null=False)
    benefit = models.CharField(null=False, max_length=100)
    date_received = models.DateField(null=False)
    date_entered = models.DateField(null=False)
    invoiced_amount = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    amount_payable = models.DecimalField(null=False, max_digits=15, decimal_places=2)

    class Meta:
        app_label = 'claims'
        db_table = "mb_claims_experience"
