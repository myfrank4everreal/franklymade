from django.shortcuts import render
from .models import AddProject
from django.core.mail import send_mail





def portinfo_home(request):
    
    return render(request, 'portinfo/portinfo_home.html')
    

def allProjects(request):
    all_project = AddProject.objects.all()
    context = {'all_project':all_project}
    return render(request, 'portinfo/allprojects.html', context)

def projectDetails(request):
    
    return render(request, 'portinfo/projectdetails.html')
    

def contactMe(request):
    if request.method == "POST":
        message_name  = request.POST['name']
        message_email  = request.POST['email']
        message = request.POST['message']
        message_phone = request.POST['phone']
        


        # import the send_mail from django.core.mail

        send_mail(
            message_name,
            message,        
            message_email, 
            ['franklin.okolie4@gmail.com'],
            )
            

       



        return render(request, 'portinfo/contact.html', {'message_name':message_name})
    else:
        return render(request, 'portinfo/contact.html', {})


    
    

