from rest_framework import serializers
from .models import County, Institution, TypeInstitution
#from address_api.models import County
from utils import code_error, message_error
from datetime import datetime as dt
from django.utils import timezone

class TypeInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeInstitution
        fields = ['id', 'description']


class ListInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class SaveInstitutionSerializer(serializers.ModelSerializer):
    county = serializers.IntegerField(write_only=True)
    type = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Institution
        fields = ('name', 'email','phone','county','street','type')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if Institution.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError(error_message.exists('name'))
            
        if Institution.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists('email'))
        
        if Institution.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists('phone'))
        return attrs
        
    def create(self, validated_data):        
        data = {
            'name': validated_data['name'],
            'email': validated_data['email'],
            'phone': validated_data['phone'],
            'county': County.objects.get(id=validated_data['county']),
            'street': validated_data['street'],
            'code': 'NA',
            #'code': validated_data['code'],
            'type': TypeInstitution.objects.get(id=validated_data['type'])
        }
        
        institution = Institution.objects.create(**data)
        
        return institution


class UpdateInstitutionSerializer(serializers.ModelSerializer):
    county = serializers.IntegerField(write_only=True)
    type = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Institution
        fields = ('name', 'email','phone','county','street','type')
    
    '''def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if Institution.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError(error_message.exists('name'))
            
        if Institution.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists('email'))
        
        if Institution.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists('phone'))
        return attrs'''
    
    def update(self, instance, validated_data):
        #county_id = validated_data['county'] if validated_data['county'] != None else 
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.county = County.objects.get(id=validated_data['county']) if validated_data['county'] != None else instance.county
        instance.street = validated_data.get('street', instance.street)
        #instance.code = validated_data.get('code', instance.code)
        instance.type = TypeInstitution.objects.get(id=validated_data['type']) if validated_data['type'] != None else instance.type
        #instance.update_date = dt.now()
        instance.update_date = timezone.now()
        
        instance.save()
        
        return instance




'''class SaveProviderSerializer(serializers.Serializer):
    institution = SaveInstitutionSerializer()
    nif = serializers.CharField(max_length=20, allow_null=False, allow_blank=False)    
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if Provider.objects.filter(nif=attrs['nif']).exists():
            raise serializers.ValidationError(error_message.exists('NIF'))
        return super().validate(attrs)

    def create(self, validated_data):  
        institutionSerializer = SaveInstitutionSerializer(data=validated_data['institution'])
        
        if institutionSerializer.is_valid():
            institutionSerializer.save()
        
            data = {
                'nif': validated_data['nif'],
                'institution': Institution.objects.get(name=institutionSerializer.data['name'])
            }
            
            provider = Provider.objects.create(**data)

            return provider
        
        return None


class ListProviderSerializer(serializers.ModelSerializer):
    institution = serializers.SlugRelatedField(queryset=Institution.objects.all(), slug_field='name')
    
    class Meta:
        model = Provider
        fields = '__all__'

class ListProviderSerializer(serializers.Serializer):
    nif slug_field='name'
    creation_date
    modified_date
    id = serializers.IntegerField()
    institution_id
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_blank=True, allow_null=True)
    phone = serializers.CharField(max_length=20, allow_blank=True, allow_null=True)
    county = serializers.IntegerField(write_only=True)
    street = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    code = serializers.CharField(max_length=10)
    type_institution = serializers.CharField()'''
