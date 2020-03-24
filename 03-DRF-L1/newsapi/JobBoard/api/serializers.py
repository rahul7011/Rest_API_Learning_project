from rest_framework import serializers
from JobBoard.models import JobOffer

###### serializer method ############
class JobOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name=serializers.CharField()
    company_email=serializers.EmailField()
    job_title = serializers.CharField()
    job_description = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    salary = serializers.IntegerField()
    available = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return JobOffer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.company_email = validated_data.get('company_email', instance.company_email)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.job_description = validated_data.get('job_description', instance.job_description)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)                                                      
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance


    # CUSTOM VALIDATERS
    def validate(self, data):
    # check that description and title are different 
    #https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
    
        if data["job_title"] == data["job_description"]:
            raise serializers.ValidationError("job_Title and job_Description must be different from one another!")
        return data

    def validate_job_description(self, value):
        #check that title is at least 60 chars long
        #https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
       
            if len(value) < 120:
                raise serializers.ValidationError("The job_description has to be at least 120 chars long!")
            return value
