from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListStudentsRegistredInCourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Show all the students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Show all Courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    """Show all Registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationStudent(generics.ListAPIView):
    """Show all registrations of one student"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer

class ListStudentsRegistredInCourse(generics.ListAPIView):
    """"Show all students resgistred in a course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsRegistredInCourseSerializer