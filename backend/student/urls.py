from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, TeacherViewSet


router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'teacher', TeacherViewSet, basename='teacher')

urlpatterns = router.urls
