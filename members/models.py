from django.db import models


# Create your models here.
class MemberDetails(models.Model):
    scheme_code = models.CharField(null=False, max_length=20)
    family_no = models.CharField(null=False, max_length=50, )
    member_no = models.CharField(primary_key=True, max_length=50, null=False)
    member_name = models.CharField(null=False, max_length=100)
    member_status = models.CharField(null=False, max_length=15)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    mobile_no = models.CharField(null=True, max_length=15)
    anniv = models.IntegerField(null=False)

    class Meta:
        managed = False
        app_label = 'members'
        db_table = 'memberDetails'


class CoverBenefits(models.Model):
    scheme_code = models.CharField(null=False, max_length=20)
    family_no = models.CharField(null=False, max_length=20)
    member_no = models.CharField(null=False, max_length=20, primary_key=True)
    benefit = models.CharField(null=False, max_length=50, primary_key=True)
    benefit_code = models.IntegerField(null=True)
    benefit_limit = models.DecimalField(null=False, default=0, decimal_places=2, max_digits=15)
    waiting_period = models.IntegerField(null=True, default=0)
    anniv = models.IntegerField(null=False, primary_key=True)
    reserves = models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)
    expenditure = models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)
    balance = models.DecimalField(null=True, default=0, max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        app_label = 'memberBenefits'
        db_table = 'coverBenefits'
