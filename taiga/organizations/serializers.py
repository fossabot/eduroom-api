from taiga.base.api import serializers
from taiga.base.fields import Field


class OrganizationSerializer(serializers.LightSerializer):
    id = Field()
    name = Field()
    location = Field()
