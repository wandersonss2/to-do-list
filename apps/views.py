from django.shortcuts import render
from .models import Tarefas

def index(request):
    tarefas = Tarefas.objects.all()
    return render(request,"index.html", {"tarefas": tarefas})

def save(request):
    tarefas1 = request.POST.get("tarefas")
    Tarefas.objects.create(tarefa=tarefas1)
    tarefas = Tarefas.objects.all()
    return render(request, "index.html", {"tarefas": tarefas})

def status(request, id):
    tarefas = Tarefas.objects.get(id=id)
    return render(request,"status.html", {"tarefas": tarefas})