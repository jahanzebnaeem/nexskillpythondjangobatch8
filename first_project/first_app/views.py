from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    # my_dict = {'insert_me': "I am pleased to be here"}
    # return render(request, 'index.html', context=my_dict)
    return render(request, 'first_app/index.html')
