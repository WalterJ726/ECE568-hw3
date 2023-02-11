from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from . import models
from catalog.forms import LoginForm, RegisterModelForm

def index(request):
    return render(
        request,
        'index.html',
        {},
    )


def register(request):
    """Register a new user."""
    if request.method == 'GET':
        # Display blank registration form.
        form = RegisterModelForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    # Process completed form.
    form = RegisterModelForm(data=request.POST)
    context = {'form': form}
    if form.is_valid():
        new_user = form.save()
        # Log the user in, and then redirect to home page.
        # authenticated_user = authenticate(username=new_user.username,
        #                                     password=request.POST['password1'])
        # login(request, authenticated_user)
        return redirect('/catalog/login/')
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'GET':        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    ## method == POST
    form = LoginForm(data=request.POST)
    if form.is_valid():
        ## the form is not empty
        print(form.cleaned_data)
        admin_object = models.User.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "incorrect username or password")
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return HttpResponse("submit successful")
    return render(request, 'login.html', {'form': form})