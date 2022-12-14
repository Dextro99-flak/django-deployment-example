from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from main_app.models import Task
from main_app.forms import TaskForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def index(request):
    task_list = Task.objects.order_by('id').all()
    form = TaskForm()
    context = {'task_list': task_list, 'form': form}
    return render(request, 'main_app/index.html', context=context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = Task(text=form.cleaned_data['text'], complete=False)
            obj.save()
    return redirect('index_page')


@login_required
def delete_task(request):
    tasks = Task.objects.filter(complete__exact=True).delete()
    return redirect('index_page')


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.complete=True
    task.save()
    return redirect('index_page')


@login_required
def delete_all(request):
    tasks = Task.objects.all().delete()
    return redirect('index_page')


def register(request):
    registered = False
    if request.method == 'POST' :
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=ProfileForm()

    return render(request, 'main_app/register.html', context={'user_form':user_form, 'user_profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active :
                login(request, user)
                return HttpResponseRedirect(reverse('index_page'))
            else:
                return HttpResponse('USER ACCOUNT IS NOT ACTIVE')
        else:
            return HttpResponse('INVALID LOGIN DETAILS')
    else:
        return render(request,'main_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_page'))