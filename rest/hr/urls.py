from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('event/', views.event_list),
    path('event/<int:pk>/', views.event_detail),
    path('member/', views.member_list),
    path('member/<code>/', views.member_detail),
    path('register/<int:pk>/', views.event_register_member),
    path('success/', views.success_member_list),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)