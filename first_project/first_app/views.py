from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    # my_dict = {'insert_me': "I am pleased to be here"}
    # return render(request, 'index.html', context=my_dict)
    # return render(request, 'first_app/index.html')
    topic_list = Topic.objects.all()
    my_topic_dict = {'topic_title': topic_list}
    return render(request, 'first_app/index.html', context=my_topic_dict)

def form_index(request):
    return render(request, 'first_app/form_index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("Validation successful")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form':form})
