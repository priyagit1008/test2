
from .models import manager_table
# django import
from rest_framework import serializers
# from rest_framework import validated_data
from rest_framework.validators import UniqueValidator

class adduserSerializer(serializers.Serializer):
    manager_id=serializers.UUIDField(required=False)
    Name= serializers.CharField()
    email= serializers.EmailField()
    password= serializers.CharField()
    mobile = serializers.CharField()
    address = serializers.CharField()
    is_active=serializers.BooleanField(required=False)
    create_at = serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)


    
    class Meta:
        model=manager_table
        fields='__all__'


    def create(self, validated_data):
        print (validated_data)
        return manager_table.objects.create(**validated_data)


    def update(self, instance, validated_data):
     instance.Name = validated_data.get('Name', instance.Name)
     instance.email = validated_data.get('email', instance.email)
     instance.password = validated_data.get('password', instance.password)
     instance.mobile = validated_data.get('mobile', instance.mobile)
     instance.address = validated_data.get('address', instance.address)
     instance.is_active = validated_data.get('is_active', instance.is_active)
     instance.create_at = validated_data.get('create_at', instance.create_at)
     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
     instance.save(self)
     return instance






class managerserializer(serializers.ModelSerializer):

    class Meta:
        model=manager_table
        # fields = ('Name',)
        fields='__all__'






