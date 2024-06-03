from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form, name='form'),
    path('django_form/', views.DjangoForms, name = 'django_form'),
    # path('student_form/',views.StudentForm, name = 'student_form'),
]
