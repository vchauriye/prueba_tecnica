from rest_framework import serializers
from .models import Pokemon


class PkmnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'pkm_id', 'name', 'type',
                  'height', 'weight', 'inverted_name')