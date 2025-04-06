"""
API router version 1.

This module defines an API router that dynamically imports and registers
viewsets from all api modules under the paracambialerta package.
"""

import importlib
import os
from django.urls import include, path


class ApiRouterV1:
    """
    A class that dynamically imports and registers viewsets from all api modules under paracambialerta
    """

    def __init__(self):
        self.base_dir = 'paracambialerta'
        self.urls = list()
        self.register_viewsets()

    def register_viewsets(self):
        """
        Registers viewsets from all api modules under paracambialerta
        """
        for module_name in os.listdir(self.base_dir):
            module_path = os.path.join(self.base_dir, module_name)
            if os.path.isdir(module_path) and 'api' in os.listdir(module_path):
                try:
                    v1 = importlib.import_module(f'{self.base_dir}.{module_name}.api.v1')
                    urlpatterns = getattr(v1, 'urlpatterns', [])
                    self.urls += urlpatterns
                except ImportError:
                    pass

    @property
    def urlpatterns(self):
        """
        Returns the urlpatterns for the API.
        """
        return [path('v1/', include((self.urls, 'api_v1')))]

