from django.db import models


# Create your models here.
class Member(models.Model):
    member_no = models.CharField(primary_key=True, max_length=50, null=False)
    family_no = models.CharField(max_length=50, null=False)
    scheme_code = models.CharField(null=False, max_length=10)
    member_names = models.CharField(null=False, max_length=200)
    member_status = models.CharField(null=False, max_length=15)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    mobile_no = models.CharField(null=True, max_length=20)
    anniv = models.IntegerField(null=False)

    class Meta:
        app_label = 'members'
        db_table = "member_details"


class CoverBenefits(models.Model):
    benefits = models.CharField(max_length=50, null=False, primary_key=True)
    scheme_code = models.CharField(null=False, max_length=10, primary_key=True)
    family_no = models.CharField(max_length=50, null=False, primary_key=True)
    member_no = models.CharField(max_length=50, null=False, primary_key=True)
    benefit_limit = models.DecimalField(null=False, max_digits=15, decimal_places=2, default=0.00)
    claims = models.DecimalField(null=True, max_digits=15, decimal_places=2, default=0.00)
    reserve_amount = models.DecimalField(null=False, max_digits=15, decimal_places=2, default=0.00)
    expense = models.DecimalField(null=False, max_digits=15, decimal_places=2, default=0.00)
    benefit_status = models.CharField(null=False, max_length=20)
    balance = models.DecimalField(null=False, max_digits=15, decimal_places=2, default=0.00)
    waiting_period = models.IntegerField(null=True)
    ben_code = models.IntegerField(null=True)

    class Meta:
        app_label = 'members'
        db_table = "cover_benefits"
