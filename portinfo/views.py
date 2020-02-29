from django.shortcuts import render



def portinfo_home(request):
    context = {}
    return render(request, 'portinfo/portinfo_home.html'context)
    

def allProjects(request):
    context = {}
    return render(request, 'portinfo/allprojects.html', context)

def projectDetails(request):
    context = {}
    return render(request, 'portinfo/projectDetails.html', context)

