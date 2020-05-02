from django.urls import path

from developer.apis.views.developer import DeveloperViewSet
from developer.views import DeveloperProfileViewSet


urlpatterns = [
    path('api/', DeveloperViewSet.as_view(), name="developer_api"),
    path('profile/', DeveloperProfileViewSet.as_view(), name="developer_profile"),
]