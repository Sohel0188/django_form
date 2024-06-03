from django.shortcuts import render
#from . form import contactForm
from . form import StudentData

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        return render(request,'firstapp/about.html',{'name' : name, 'email' : email})
    else:
        return render(request,'firstapp/about.html')
def contact(request):
    return render(request,'firstapp/contact.html')

def form(request):
    print(request.POST)
    return render(request,'firstapp/form.html')

def DjangoForms(request):
    # form = contactForm(request.POST, request.FILES)
    
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     file = form.cleaned_data['file']
    #     with open('./firstapp/templates/firstapp/uploads/' + file.name, 'wb+') as destination:
    #         for chunk in file.chunks():
    #             destination.write(chunk) 
    # else:
    #     form = contactForm()  
        
    form = StudentData(request.POST, request.FILES)
    if request.method == 'POST':    
        if form.is_valid():
            print(form.cleaned_data)              
        else:
            form = StudentData()
    return render(request,'./firstapp/django_form.html',{'student_form':form})


# def djangoformstest(request):
#     form = contactForm(request.POST, request.FILES)
#     if form.is_valid():
#         file = form.cleaned_data['file']
#         with open('.firstapp/templates/firstapp/uploads' + file.name, 'wb+') as destination :
#             for chunk in file.chunks():
#                 destination.write(chunk)

"""
 def djangoform(request):
    form = contactForm(request.POST, request.FILES)
    if form.is_valid():
        file = form.cleaned_data['file']
        with open('.firstapp/templates/firstapp/uploads' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    else:
        form = contactForm()
    return render ( request, '.firstapp/django_form.html',{"form":form})
 
"""

# def StudentForm(request):
#     if request.method == 'POST':
#         form = StudentData(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = StudentData()
   #return render(request, 'firstapp/django_form.html',{'student_form':form})
    
    