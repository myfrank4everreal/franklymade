from django.shortcuts import render



def portinfo_home(request):
    context = {}
    return render(request, 'portinfo/portinfo_home.html')
    