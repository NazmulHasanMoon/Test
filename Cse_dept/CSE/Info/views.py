from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'all_student_list': students})


def single_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'single_student.html', {'student': student})
