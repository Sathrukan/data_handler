from rest_framework.serializers import ModelSerializer
from .models import Account, Destination

class DestinationSerializer(ModelSerializer):
  class Meta:
    model = Destination
    fields = "__all__"

class AccountSerializer(ModelSerializer):
  destinations = DestinationSerializer(many=True, read_only=True)
  class Meta:
    model = Account
    fields = "__all__"