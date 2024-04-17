from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(...)
            else:
                return render(...)
        except:
            return redirect(...)
    return render(request, ...)

def register(request):
    if request.method == 'POST':
        try:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                models.User.objects.create_user(
                    username=username, 
                    password=password, 
                    first_name=f_name, 
                    last_name=l_name
                    )
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect(...)
        except:
            return redirect(...)
    return render(request, ...)

@login_required
def log_out(request):
    logout(request)
    return redirect(...)

def category_create(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name = request.POST['name']
        )
        return redirect(...)
    return render(request, ...)

def category_list(request):
    queryset = models.Category.objects.all()
    context = {
        'queryset':queryset
        }
    return render(request, ..., context)

def category_update(request, id):
    queryset = models.Category.objects.get(id=id)
    queryset.name = request.POST['name']
    queryset.save()
    return redirect(...)
 
def category_delete(request, id):
    queryset = models.Category.objects.get(id=id)
    queryset.delete()
    return redirect(...)
