from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views.address import (
    AddressCreateView, AddressDetailsView,
    CityCreateView, CityDetailsView,
    CountryCreateView, CountryDetailsView)
from .views.ammenity import AmmenityCreateView, AmmenityDetailsView
from .views.files import FileView
from .views.floor_plan import FloorPlanCreateView, FloorPlanDetailsView
from .views.picture import PictureCreateView, PictureDetailsView
from .views.profile import (
    ProfileListView, ProfileCreateView, ProfileDetailsView)
from .views.property import PropertyCreateView, PropertyDetailsView
from .views.review import ReviewCreateView, ReviewDetailsView
from .views.user import UserCreateView, UserDetailsView


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
        'addresses/',
        AddressCreateView.as_view(),
        name="addresses"
    ),
    path(
        'addresses/<int:pk>/',
        AddressDetailsView.as_view(),
        name="address_details"
    ),
    path(
        'ammenities/',
        AmmenityCreateView.as_view(),
        name="ammenities"
    ),
    path(
        'ammenities/<int:pk>/',
        AmmenityDetailsView.as_view(),
        name="ammenity_details"
    ),
    path(
        'cities/',
        CityCreateView.as_view(),
        name="cities"
    ),
    path(
        'cities/<int:pk>/',
        CityDetailsView.as_view(),
        name="city_details"
    ),
    path(
        'countries/',
        CountryCreateView.as_view(),
        name="countries"
    ),
    path(
        'countries/<int:pk>/',
        CountryDetailsView.as_view(),
        name="country_details"
    ),
    path(
        'floor-plans/',
        FloorPlanCreateView.as_view(),
        name="floorplans"
    ),
    path(
        'floor-plans/<int:pk>/',
        FloorPlanDetailsView.as_view(),
        name="floorplan_details"
    ),
    path(
        'files/upload/',
        FileView.as_view(),
        name="file_upload"
    ),
    path(
        'pictures/',
        PictureCreateView.as_view(),
        name="pictures"
    ),
    path(
        'pictures/<int:pk>/',
        PictureDetailsView.as_view(),
        name="picture_details"
    ),
    path(
        'profiles/',
        ProfileListView.as_view(),
        name="profiles"
    ),
    path(
        'profiles/create/',
        ProfileCreateView.as_view(),
        name="profiles"
    ),
    path(
        'profiles/get/<int:pk>/',
        ProfileDetailsView.as_view(),
        name="profile_details"
    ),
    path(
        'properties/',
        PropertyCreateView.as_view(),
        name="properties"
    ),
    path(
        'properties/<int:pk>/',
        PropertyDetailsView.as_view(),
        name="property_details"
    ),
    path(
        'reviews/',
        ReviewCreateView.as_view(),
        name="reviews"
    ),
    path(
        'reviews/<int:pk>/',
        ReviewDetailsView.as_view(),
        name="review_details"
    ),
    path(
        'users/',
        UserCreateView.as_view(),
        name="users"
    ),
    path(
        'users/<int:pk>/',
        UserDetailsView.as_view(),
        name="user_details"
    )
}

urlpatterns = format_suffix_patterns(urlpatterns)
