from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.functional import cached_property

from django_pglocks import advisory_lock

class Organization(models.Model):
	 # This model stores all organization memberships. Also
    
    name = models.CharField(max_length=250, null=False, blank=False,
                            verbose_name=_("name"))
    location = models.CharField(max_length=250, null=False, blank=False,
                            verbose_name=_("location"))

    class Meta:
        verbose_name = "organization"
        verbose_name_plural = "organizations"
        # unique_together = ("user", "project",)
        # ordering = ["project", "user__full_name", "user__username", "user__email", "email"]
