from rest_framework import routers

from paracambialerta.user import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = router.urls
