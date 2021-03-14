from .views import ProjectViewSet, CriteriaViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"criteria", CriteriaViewSet)

urlpatterns = router.urls
