from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #this part creates a context dict to pass the template engine as its content
    #the bold message is dsame as that of the contained in the template folder
    context_dict={'boldmessage':"am learning django from the scratch"}

    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    con_dict = {'about':"About rango"}
    return render(request, 'rango/about.html', context=con_dict)