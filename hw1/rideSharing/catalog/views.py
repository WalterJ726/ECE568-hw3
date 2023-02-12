from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from . import models
from catalog.forms import LoginForm, RegisterModelForm, ownerUpdateModelForm, OrderModelForm

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
        # print(form.cleaned_data)
        admin_object = models.User.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "incorrect username or password")
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return render(request, 'index.html')
    return render(request, 'login.html', {'form': form})

def logout(request):
    request.session.clear()
    return redirect('/catalog/login/')

def ownerUpdate(request):
    """Register a new user."""
    nid = request.session['info']['id']  ## todo: 要和当前id匹配才行
    row_object = models.User.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/catalog/login/')
    
    if request.method == 'GET':
        # Display blank registration form.
        print(row_object)
        print(row_object.email)
        form = ownerUpdateModelForm(instance=row_object)
        context = {'form': form}
        return render(request, 'ownerEditProfile.html', context)

    # Process completed form.
    form = ownerUpdateModelForm(data=request.POST, instance=row_object)
    context = {'form': form}
    if form.is_valid():
        new_user = form.save()
        # Log the user in, and then redirect to home page.
        # authenticated_user = authenticate(username=new_user.username,
        #                                     password=request.POST['password1'])
        # login(request, authenticated_user)
        return redirect('/catalog/login/')
    return render(request, 'ownerEditProfile.html', context)


def ownerIndex(request):
    return render(request, 'ownerIndex.html')

def ownerNewRequest(request):

    if request.method == 'GET':
        form = OrderModelForm()
        return render(request, 'ownerNewRequest.html', {'form': form})

    ## post request
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/catalog/ownerIndex/')
    return render(request, 'ownerNewRequest.html', {'form': form})


def ownerCurrentRequest(request):
    currentRequest = models.Order.objects.all()
    context = {'currentRequest': currentRequest} 
    return render(request, 'ownerCurrentRequest.html', context)

def requestDelete(request, request_id):
    ## todo check the user id is equal to the deleter
    models.Order.objects.filter(id=request_id).delete()
    currentRequest = models.Order.objects.all()
    context = {'currentRequest': currentRequest} 
    return render(request, 'ownerCurrentRequest.html', context)

def requestEdit(request, request_id):
    editOrder = models.Order.objects.filter(id=request_id).first()
    
    if request.method == 'GET':
        form = OrderModelForm(instance=editOrder)
        context = {'form': form}
        return render(request, 'ownerNewRequest.html', {'form': form})

    # Process completed form.
    form = OrderModelForm(data=request.POST, instance=editOrder)
    context = {'form': form}
    if form.is_valid():
        editedOrder = form.save()
        # Log the user in, and then redirect to home page.
        # authenticated_user = authenticate(username=new_user.username,
        #                                     password=request.POST['password1'])
        # login(request, authenticated_user)
        return redirect('/catalog/ownerCurrentRequest/')
    return render(request, 'ownerNewRequest.html', context)


    