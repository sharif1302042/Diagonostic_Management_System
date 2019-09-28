from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from diagonostic_management.tables import DoctorTable
from .models import Doctor

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = "This is Home Page"
        return Response({'profiles': queryset})

class Dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get(self, request):
        queryset = "This is Home Page"
        return Response({'profiles': queryset})

class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        queryset = "This is Home Page"
        return Response({'profiles': queryset})

class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        queryset = "This is Home Page"
        return Response({'profiles': queryset})

class DoctorDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doctor_details.html'
    def get(self, request):
        queryset = Doctor.objects.filter(pk=1).values()
        print(queryset)
        return Response({'doctor': queryset})

class DoctorList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doctor_list.html'
    def get(self, request):
        queryset = Doctor.objects.all().values()
        print(queryset)
        return Response({'doctors': queryset})

