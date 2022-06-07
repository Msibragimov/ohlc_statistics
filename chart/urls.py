from django.urls import include, path
from rest_framework import routers
from chart import views

router = routers.SimpleRouter()
router.register(r'(?P<ticker>.+)', views.ChartsListView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
] + router.get_urls()