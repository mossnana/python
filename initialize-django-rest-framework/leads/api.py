# import class Lead from leads app models
from leads.models import Lead
# import LeadSerializer class from serializer
from leads.serializers import LeadSerializer
# viewsets and permissions library import
from rest_framework import viewsets, permissions

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
	queryset = Lead.objects.all()
	print(Lead.objects)
	# Lead.objects = leads.Lead.objects
	print(queryset)
	# queryset = <QuerySet [<Lead: Lead object (1)>]>
	permission_classes = [
   		permissions.AllowAny,
   	]
    # permissions.AllowAny = allow to public
	serializer_class = LeadSerializer

	print(serializer_class)
	# output: <class 'leads.serializers.LeadSerializer'>
