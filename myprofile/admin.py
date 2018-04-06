from django.contrib import admin

from myprofile.models import Users, UserSession

admin.site.register(Users)
admin.site.register(UserSession)
