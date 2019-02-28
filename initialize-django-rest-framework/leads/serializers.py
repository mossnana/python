from rest_framework import serializers
from leads.models import Lead

# class LeadSerializer extends ModelSerializer in serializers
class LeadSerializer(serializers.ModelSerializer):
	# Metadata 
	class Meta:
	    model = Lead
	    print(Lead)
	    # output: (class 'leads.models.Lead')
	    # output: (class 'app name.model folder.class name')
	    fields = '__all__'
	    # __all__ -> export list of public objects of that module