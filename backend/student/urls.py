from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet


router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = router.urls
