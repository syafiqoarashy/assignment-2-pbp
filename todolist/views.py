from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # data_todolist_item = Task.objects.filter(user = request.user)

    context = {
        # 'list_item' : data_todolist_item,
        'user' : request.user,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def show_test(request):
    return render(request, 'test.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title != "" and description != "":
            data = Task.objects.create(user=request.user, title=title, description=description, date=datetime.datetime.today())
            return JsonResponse({
                    "pk": data.id,
                    "fields": {
                        "title": data.title,
                        "description": data.description,
                        "is_finished": data.is_finished,
                        "date": data.date,
                    },
                },
                status=200,
            )
        else:
            messages.info(request, 'Please fill the title/description!')

    context = {}    
    return render(request, 'createtask.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    selected = Task.objects.get(user = request.user, id=id)
    selected.delete()
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def complete_task(request, id):
    selected = Task.objects.get(user = request.user, id=id)
    selected.is_finished = not selected.is_finished
    selected.save()
    return redirect('todolist:todolist')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_data_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")