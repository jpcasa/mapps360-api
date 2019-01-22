from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views.property import PropertyCreateView, PropertyDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    path(
        'auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    path(
        'get-token/',
        obtain_auth_token
    ),
    path(
        'properties/',
        PropertyCreateView.as_view(),
        name="createProperty"
    ),
    path(
        'properties/<int:pk>/',
        PropertyDetailsView.as_view(),
        name="detailsProperty"
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
