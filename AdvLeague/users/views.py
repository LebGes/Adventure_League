from django.shortcuts import render

# Create your views here.

def users_lk(request):
    return render(request, 'users/index.html')
