from django.urls import path

from .views import (
    RegisterUserAPI,
    ObtainTokenAPI,
    ViewUserAPI
)
urlpatterns = [
    path('create/', RegisterUserAPI.as_view(), name='user-create'),
    path('token/', ObtainTokenAPI.as_view(), name='access-token'),
    path('me/', ViewUserAPI.as_view(), name='me')
]
