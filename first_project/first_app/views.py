from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    # my_dict = {'insert_me': "I am pleased to be here"}
    # return render(request, 'index.html', context=my_dict)
    # return render(request, 'first_app/index.html')
    topic_list = Topic.objects.all()
    my_topic_dict = {'topic_title': topic_list}
    return render(request, 'first_app/index.html', context=my_topic_dict)
