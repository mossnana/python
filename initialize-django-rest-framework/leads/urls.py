from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
print(urlpatterns)
"""
Output:
[<URLPattern '^api/leads/$' [name='leads-list']>, <URLPatormat>[a-z0-9]+)/?$' [name='leads-list']>, <URLPattern '^
)/$' [name='leads-detail']>, <URLPattern '^api/leads/(?P<
[a-z0-9]+)/?$' [name='leads-detail']>, <URLPattern '^$' [
Pattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>]

"""