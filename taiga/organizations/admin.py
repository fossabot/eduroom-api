from django.contrib import admin
from . import models

class OrganizationList(admin.ModelAdmin):
	list_display = ["name", "location",]

admin.site.register(models.Organization, OrganizationList)
