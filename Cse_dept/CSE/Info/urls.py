from django.urls import path
from Info import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('student-list/', views.student_list, name='student-list'),
    path('single-student/<student_id>/', views.single_student, name='single-student'),
    path('teacher-list/', views.teacher_list, name='teacher-list'),
    path('single-teacher/<teacher_id>/', views.single_teacher, name='single-teacher'),
]