
from .models import myclients
# django import
from rest_framework import serializers
# from rest_framework import validated_data
from rest_framework.validators import UniqueValidator


class addclientSerializer(serializers.Serializer):
    client_id=serializers.UUIDField(required=False)
    client_name= serializers.CharField()
    contact_email= serializers.EmailField()
    number= serializers.CharField()
    address = serializers.CharField()
    is_active=serializers.BooleanField(required=False)
    create_at = serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)



    def create(self, validated_data):
        return myclients.objects.create(**validated_data)

   
    def update(self, instance, validated_data):
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.contact_email= validated_data.get('contact_email', instance.contact_email)
        instance.number = validated_data.get('number', instance.number)
        instance.address = validated_data.get('address', instance.address)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


    
    class Meta:
        model=myclients
        fields='__all__'


class clientserializer(serializers.ModelSerializer):

    class Meta:
        model=myclients
        # fields = ('Name',)
        fields='__all__'
