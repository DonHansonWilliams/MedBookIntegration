from django.db import models


# Create your models here.

class Member(models.Model):
    scheme_code = models.CharField(null=False)
    family_no = models.CharField(null=False)
    member_no = models.CharField(primary_key=True, null=False)
    member_names = models.CharField(null=False, max_length=100)
    member_status = models.CharField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    mobile_no = models.DateField(null=False, max_length=20)
    anniv = models.IntegerField(null=False, max_length=2)

    class Meta:
        app_label = "members"
        db_table = "medbook_member_details"
