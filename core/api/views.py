from .models import Container
import docker

from django.contrib.auth import authenticate, login as login_, logout as logut_
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
client = docker.from_env()

def login(request: HttpRequest):
    
    template_name = "api/login.html"
    user: User = request.user

    if user.is_authenticated:
        return redirect("dashboard")

    if request.method == "GET":
        return render(request=request, template_name=template_name)
    if request.method == "POST":
        data = request.POST
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user:
            login_(request, user)
            return redirect("dashboard")
        return render(request=request, template_name=template_name)

def signup(request: HttpRequest):
    template_name = "api/signup.html"
    user: User = request.user

    if user.is_authenticated:
        return redirect("dashboard")

    if request.method == "GET":
        return render(request=request, template_name=template_name)
    if request.method == "POST":
        data = request.POST
        username = data.get("username", None)
        password = data.get("password", None)
        user = User.objects.create_user(username=username, password=password)
        if user:
            return redirect("login")
        return render(request=request, template_name=template_name)

@login_required(login_url="/api/login/")
def dashboard(request: HttpRequest):

    user: User = request.user
    template_name="api/dashboard.html"

    if request.method == "GET":
        containers = user.containers.all()
        context = {
            "containers": containers
        }
        return render(request=request, context=context, template_name=template_name)
    
    if request.method == "POST":

        container_object = Container.objects.order_by("created_on").last()
        if container_object:
            container_port = container_object.port + 2
        else:
            container_port = 5000

        container = client.containers.run(
            image="uv",
            ports={
                '22/tcp': container_port,
                '80/tcp': container_port + 1
            },
            detach=True,
            stdin_open=True,
            auto_remove=True
        )

        print(f">>> {container.id} started")
        user.containers.create(container_id=container.id, port=container_port)
        return redirect("dashboard")

@login_required(login_url="/api/login/")
def stop_container(request: HttpRequest):

    user: User = request.user

    if request.method == "POST":
        data = request.POST
        container_id = data.get("id", None)
        container = client.containers.get(container_id=container_id)
        container.stop()
        user.containers.get(container_id=container_id).delete()
        return redirect("dashboard")

@login_required(login_url="/api/login/")
def logout(request: HttpRequest):
    logut_(request)
    return redirect("login")
