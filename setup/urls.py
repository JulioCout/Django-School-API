from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationViewSet, ListRegistrationStudent, ListStudentsRegistredInCourse
from rest_framework import routers

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Julio's School Management API",
      default_version='v1',
      description="System to manage students, classes and registration of a school.",
      terms_of_service="@",
      contact=openapi.Contact(email="juliocscoutinho@outlook.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('Students', StudentsViewSet, basename='Students')
router.register('Courses', CoursesViewSet, basename='Courses')
router.register('Registrations', RegistrationViewSet, basename='Registration')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('students/<int:pk>/registrations/', ListRegistrationStudent.as_view()),
   path('courses/<int:pk>/registrations/', ListStudentsRegistredInCourse.as_view()),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
