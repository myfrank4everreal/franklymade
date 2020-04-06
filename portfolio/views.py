from django.shortcuts import render, redirect
from .models import PythonTutorial
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# for the franklymade homepage
def franklymade_home(request):
    context = {}
    return render(request, 'sitetemplate/base.html', context)

# for the search bar
# i still need to work on this function for it to be able to find the required keyword
def searchBar(request):
    keyword_list = ['python', 'django', 'javascript'] 
    if keyword_list.Find['python']:

        return render(request, 'portfolio/python_intro.html', context)
    elif keyword_list.Find['django']:
        return render(request, 'sitetemplate/djangobase.html', context)
    else:
        return render(request, 'sitetemplate/base.html', context)


            





# ******************************************
# for the python tutorials
def python_intro(request):   
    context = {}
    return render(request, 'portfolio/python_intro.html', context)


def python_cours_details(request, course_id):
    try:
        course = PythonTutorial.objects.get(pk=course_id)
       
       
    except:
        return redirect('python_intro')
       

    else:
        
        

       
    


        # if course.DoesNotExist:
        #     return redirect('python_intro')

            
        if course.id == 27:
            context = {'course':course}
            return render(request, 'portfolio/variable_and_datatype.html', context)
        elif course_id == 28:
            context = {'course':course}
            return render(request, 'portfolio/operators_and_input.html', context)
        elif course_id == 29:
            context = {'course':course}
            return render(request, 'portfolio/conditions.html', context)
        elif course_id == 30:
            context = {'course':course}
            return render(request, 'portfolio/if_else.html', context)
        elif course_id == 31:
            context = {'course':course}
            return render(request, 'portfolio/nested_statements.html', context)
        elif course_id == 32:
            context = {'course':course}
            return render(request, 'portfolio/forloops.html', context)
        elif course_id == 33:
            context = {'course':course}
            return render(request, 'portfolio/whileloops.html', context)
        elif course_id == 34:
            context = {'course':course}
            return render(request, 'portfolio/listandtuple.html', context)
    

        elif course_id == 35:
            context = {'course':course}
            return render(request, 'portfolio/string_method.html', context)
        elif course_id == 36:
            context = {'course':course}
            return render(request, 'portfolio/slice_operator.html', context)
        elif course_id == 37:
            context = {'course':course}
            return render(request, 'portfolio/functions.html', context)
        elif course_id == 38:
            context = {'course':course}
            return render(request, 'portfolio/reading_files.html', context)
        elif course_id == 39:
            context = {'course':course}
            return render(request, 'portfolio/writing_files.html', context)
        elif course_id == 40:
            context = {'course':course}
            return render(request, 'portfolio/listmethod.html', context)
        elif course_id == 41:
            context = {'course':course}
            return render(request, 'portfolio/modular_programing.html', context)
        elif course_id == 42:
            context = {'course':course}
            return render(request, 'portfolio/error_handling.html', context)
        elif course_id == 43:
            context = {'course':course}
            return render(request, 'portfolio/global_vs_local.html', context)
        elif course_id == 44:
            context = {'course':course}
            return render(request, 'portfolio/classes_and_objects.html', context)
        # else:
            # return HttpResponseRedirect(reverse('python_intro', args=(course.id,)))

    return redirect('python_intro')
    
    

# search function
# def searchCourse(request):





    

# def viewPortfolio(request):
    
#     context = {'projects':projects}
#     return render(request, 'portfolio/listandtuple.html', context)


# for django tutorial
def django_intro(request):
    context = {}
    return render(request, 'sitetemplate/djangobase.html', context)