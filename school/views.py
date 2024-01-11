from rest_framework import viewsets
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    "Show all the students"
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    "Show all Courses"
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    "Show all Registrations"
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer