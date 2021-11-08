from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos',TodoViewSet)

urlpatterns = router.urls

# import pprint
# pprint.pprint(router.get_urls())