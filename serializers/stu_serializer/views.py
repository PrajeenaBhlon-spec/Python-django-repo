from django.shortcuts import render
from .serializers import student_serializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def display(request):
  if request.method == "GET":
    students = Student.objects.all()
    serializer = student_serializer(students , many = True)
    return render(request , "show.html" , {"students" :serializer.data})