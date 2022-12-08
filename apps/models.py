from django.db import models

# Create your models here.

class Tarefas(models.Model):
    tarefa = models.CharField(max_length=200)

    def __str__(self):
        return self.tarefa