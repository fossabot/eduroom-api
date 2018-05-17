from taiga.base.api import validators

from . import models


class OrganizationValidator(validators.ModelValidator):
    class Meta:
        model = models.Organization
        fields = ("id", "name", "project")
