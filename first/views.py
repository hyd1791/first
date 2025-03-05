from django.shortcuts import render

def home(request):
    context = {'name1':'함영도',
               'name2' :'곱창',
               'name3' : '아무개',}
    return render(request,'first/home.html', context)
# Create your views here.
