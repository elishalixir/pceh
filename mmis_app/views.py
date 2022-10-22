from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import NewRegistration, MapForm, LoginForm
from .models import MercuryAddedProducts
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'mmis_app/welcome.html')


def sign_up(request):
    if request.method == 'POST':
        form = NewRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/welcome')
    else:
        form = NewRegistration()
        return render(request, 'registration/sign_up.html', {'form': form})

    return render(request, 'registration/login.html')


def login_view(request):
    form = LoginForm(request.POST)
    msg = ''
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.role:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.sector:
                login(request, user)
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


# @login_required(login_url='/login')
def welcome(request):
    return render(request, 'mmis_app/welcome.html')


# MercuryAddedProducts

# @login_required(login_url='/login')
# READ
def map_read(request):
    context = {'map_read':MercuryAddedProducts.objects.all()}
    return render(request, 'mmis_app/map/map_read.html', context)


# CREATE/UPDATE
def map_create(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/map_read')
            except:
                pass
    else:
        form = MapForm()
    return render(request, "mmis_app/map/map_create.html", {'form': form})

#EDIT
def map_edit(request, map_id):
    map = MercuryAddedProducts.objects.get(map_id=map_id)
    return render(request, "mmis_app/map/map_edit.html", {'map': map})

def map_update(request, map_id):
    map = MercuryAddedProducts.objects.get(map_id=map_id)
    form = MapForm(request.POST, instance=map)
    if form.is_valid():
        try:
            form.save()
            print(form.errors)
            return redirect('/map_read')
        except:
            pass
    return render(request, "mmis_app/map/map_edit.html", {'form': form})

# DELETE
def map_delete(request, map_id):
    map = MercuryAddedProducts.objects.get(map_id=map_id)
    map.delete()
    return redirect('/map_read')


# @login_required(login_url='/login')
def contact(request):
    pass


# @login_required(login_url='/login')
def feedback(request):
    return render(request, "mmis_app/feedback.html")


@login_required(login_url='/login')
def health(request):
    pass


@login_required(login_url='/login')
# @permission_required('ASGMElisha', raise_exception=True)
def Asgm(request):
    pass


@login_required(login_url='/login')
def cement_sector(request):
    pass


@login_required(login_url='/login')
def energy_fuel(request):
    pass
