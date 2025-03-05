from django.shortcuts import render

def home(request):
    context = {'name':'함영도',
               'hobby' :'곱창',
               'interest' : '아무개',}
    return render(request,'first/home.html', context)
# Create your views here.
