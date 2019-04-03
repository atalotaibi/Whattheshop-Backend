from django.urls import path
from .views import (
    UserCreateAPIView,
    CategorysList,
    ProfileDetailView,
    ProfileUpdateView,
    AddressListlView,
    AddressUpdateView,
    AddressDeleteView,
    AddressCreateView,


)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CategorysList/', CategorysList.as_view(), name='CategorysList'),
    path('<int:profile_id>/detail/', ProfileDetailView.as_view(), name='api-detail'),
    path('<int:profile_id>/update/', ProfileUpdateView.as_view(), name='api-update'),
    path('<int:profile_id>/addesslist/', AddressListlView.as_view(), name='addess-list'),
    path('<int:address_id>/addessupdate/', AddressUpdateView.as_view(), name='addess-update'),
    path('<int:address_id>/addesscreate/', AddressDeleteView.as_view(), name='addess-delete'),
    path('<int:address_id>/addessdelete/', AddressCreateView.as_view(), name='addess-create'),
]
