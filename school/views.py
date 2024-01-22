from rest_framework import viewsets, generics, status
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, StudentSerializerV2, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListStudentsRegistredInCourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

class StudentsViewSet(viewsets.ModelViewSet):
    """Show all the students"""
    queryset = Student.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    def get_serializer_class(self):
        if self.request.version == "v2":
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Show all Courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response



class RegistrationViewSet(viewsets.ModelViewSet):
    """Show all Registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ListRegistrationStudent(generics.ListAPIView):
    """Show all registrations of one student"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ListStudentsRegistredInCourse(generics.ListAPIView):
    """"Show all students resgistred in a course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsRegistredInCourseSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]