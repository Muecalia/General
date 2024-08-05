from rest_framework import serializers
from . import models as m



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Country
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Province
        fields = '__all__'
        

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.County
        fields = '__all__'

