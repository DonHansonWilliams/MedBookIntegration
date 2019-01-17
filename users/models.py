from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(primary_key=True, null=False, max_length=100)
    user_pass = models.CharField(null=False, max_length=100)

    class Meta:
        managed = False
        app_label = 'users'
        db_table = "mb_users"
