from rest_framework import routers

from paracambialerta.user.interface.views import (
    UserViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
