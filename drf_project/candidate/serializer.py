from.models import mycandidates

from rest_framework import serializers

from rest_framework.validators import UniqueValidator
import datetime

class addcandidateserializer(serializers.Serializer):
	candidate_id=serializers.UUIDField(required=False)
	Name=serializers.CharField()
	email=serializers.EmailField()
	number=serializers.CharField()
	address=serializers.CharField()
	is_active=serializers.BooleanField(required=False)
	current_ctc=serializers.IntegerField()
	expected_ctc=serializers.IntegerField()
	notice_days=serializers.IntegerField()
	is_alredy_on_notice=serializers.BooleanField()
	tech_skills=serializers.CharField()
	preferable_location=serializers.CharField()
	create_at = serializers.DateTimeField(required=False)
	updated_at= serializers.DateTimeField(required=False)

	class Meta:
		model=mycandidates
		fields='__all__'

	def create(self,validated_data):
		return mycandidates.objects.create(**validated_data)

	
	def update(self, instance, validated_data):
		instance.Name = validated_data.get('Name', instance.Name)
		instance.email= validated_data.get('email', instance.email)
		instance.number = validated_data.get('number', instance.number)
		instance.address = validated_data.get('address', instance.address)
		instance.is_active = validated_data.get('is_active', instance.is_active)
		instance.current_ctc = validated_data.get('current_ctc', instance.current_ctc)
		instance.expected_ctc = validated_data.get('expected_ctc', instance.expected_ctc)
		instance.notice_days = validated_data.get('notice_days', instance.notice_days)
		instance.is_alredy_on_notice = validated_data.get('is_alredy_on_notice', instance.is_alredy_on_notice)
		instance.tech_skills = validated_data.get('tech_skills', instance.tech_skills)
		instance.preferable_location = validated_data.get('preferable_location', instance.preferable_location)

		instance.create_at = validated_data.get('create_at', instance.create_at)

		instance.updated_at = validated_data.get('updated_at', instance.updated_at)

		instance.save()
		return instance



	