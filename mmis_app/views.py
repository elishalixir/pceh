from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import NewRegistration, MapForm, LoginForm, EnergyFuelForm, CementForm
from .models import MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement
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
            if user is not None and user.is_health:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_cement:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_asgm:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_EandF:
                login(request, user)
                return redirect('welcome')
            if user is not None and user.is_map:
                login(request, user)
                return redirect('welcome')

            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


@login_required(login_url='/login')
def welcome(request):
    return render(request, 'mmis_app/welcome.html')


# MercuryAddedProducts


# READ
@login_required(login_url='/login')
def map_read(request):
    context = {'map_read':MercuryAddedProducts.objects.all()}
    return render(request, 'mmis_app/map/map_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def map_create(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/map_read')
            except:
                pass
    else:
        form = MapForm()
    return render(request, "mmis_app/map/map_create.html", {'form': form})

#EDIT
@login_required(login_url='/login')
def map_edit(request, map_id):
    map = MercuryAddedProducts.objects.get(map_id=map_id)
    return render(request, "mmis_app/map/map_edit.html", {'map': map})


@login_required(login_url='/login')
def map_update(request, map_id):
    map = MercuryAddedProducts.objects.get(map_id=map_id)
    form = MapForm(request.POST, instance=map)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/map_read')
        except:
            pass
    return render(request, "mmis_app/map/map_edit.html", {'form': form})


# DELETE
@login_required(login_url='/login')
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


@login_required(login_url='/login')
def ecfp_read(request):
    context = {'ecfp_read':EnergyConsumptionAndFuelProduction.objects.all()}
    return render(request, 'mmis_app/energyfuel/ecfp_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def ecfp_create(request):
    if request.method == 'POST':
        form = EnergyFuelForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/ecfp_read')
            except:
                pass
    else:
        form = EnergyFuelForm()
    return render(request, "mmis_app/energyfuel/ecfp_create.html", {'form': form})

#EDIT
@login_required(login_url='/login')
def ecfp_edit(request, ecfp_id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(ecfp_id=ecfp_id)
    return render(request, "mmis_app/energyfuel/ecfp_edit.html", {'ecfp': ecfp})


@login_required(login_url='/login')
def ecfp_update(request, ecfp_id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(ecfp_id=ecfp_id)
    form = EnergyFuelForm(request.POST, instance=ecfp)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/ecfp_read')
        except:
            pass
    return render(request, "mmis_app/energyfuel/ecfp_edit.html", {'form': form})

# DELETE
@login_required(login_url='/login')
def ecfp_delete(request, ecfp_id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(ecfp_id=ecfp_id)
    ecfp.delete()
    return redirect('/ecfp_read')

#cement
@login_required(login_url='/login')
def cem_read(request):
    context = {'cem_read': Cement.objects.all()}
    return render(request, 'mmis_app/cement/cem_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def cem_create(request):
    if request.method == 'POST':
        form = CementForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/cem_read')
            except:
                pass
    else:
        form = CementForm()
    return render(request, "mmis_app/cement/cem_create.html", {'form': form})

#EDIT
@login_required(login_url='/login')
def cem_edit(request, cem_id):
    cem = Cement.objects.get(cem_id=cem_id)
    return render(request, "mmis_app/cement/cem_edit.html", {'cem': cem})


@login_required(login_url='/login')
def cem_update(request, cem_id):
    cem = Cement.objects.get(cem_id=cem_id)
    form = CementForm(request.POST, instance=cem)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/cem_read')
        except:
            pass
    return render(request, "mmis_app/cement/cem_edit.html", {'form': form})

# DELETE
@login_required(login_url='/login')
def cem_delete(request, cem_id):
    cem = Cement.objects.get(cem_id=cem_id)
    cem.delete()
    return redirect('/cem_read')