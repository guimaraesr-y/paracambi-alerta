"""
API router.

This module contains the API router which is responsible for registering and
providing the versioned API endpoints.
"""

from django.urls import path, include
from paracambialerta.api.api_v1 import ApiRouterV1


router_v1 = ApiRouterV1()

urlpatterns = [
    path('', include((router_v1.urlpatterns, 'api_v1'))),
]
