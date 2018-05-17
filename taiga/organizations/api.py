from taiga.base.api import ModelCrudViewSet

from . import permissions
from . import models
from . import serializers
from . import validators

######################################################
# Organizations
######################################################


class OrganizationsViewSet(ModelCrudViewSet):
	permission_classes = (permissions.OrganizationPermission,)
	serializer_class = serializers.OrganizationSerializer
	validator_class = validators.OrganizationValidator
	model = models.Organization

	def is_blocked(self, obj):
		return obj.blocked_code is not None
