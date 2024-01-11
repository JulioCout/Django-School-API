from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationViewSet, ListRegistrationStudent, ListStudentsRegistredInCourse
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Students', StudentsViewSet, basename='Students')
router.register('Courses', CoursesViewSet, basename='Courses')
router.register('Registrations', RegistrationViewSet, basename='Registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', ListRegistrationStudent.as_view()),
    path('course/<int:pk>/registrations/', ListStudentsRegistredInCourse.as_view())
]
