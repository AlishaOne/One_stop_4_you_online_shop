from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=50)
    confpassword = models.CharField(max_length=50)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name


class UserSession(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.PROTECT)
    # session=models.ForeignKey(Session,null=True,blank=True,on_delete=models.SET_NULL)

    user_id = models.CharField(max_length=100, db_index=True)
    session_id = models.CharField(max_length=200, db_index=True)
    session_data = models.TextField(max_length=1024, null=True, blank=True)

    class Meta:
        unique_together = ("id", "user_id")

    def __str__(self):
        # return "{}-{}-{}".format(str(self.id),self.user_id,self.session_data)
        return "{}".format(self.id)
