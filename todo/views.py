from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from todo.forms import PostForm
from .models import Todo
# Create your views here.

class TodoListView(ListView):
    model = Todo

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'priority')
        # validate ordering here
        return ordering






class TodoCreateView(CreateView):
    model = Todo
    form_class = PostForm
    # fields = ['priority','title','content','due_date','success']
    success_url = reverse_lazy('list')
    template_name_suffix = "_create"

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = PostForm
    #fields = ['priority','title','content','due_date','success']
    template_name_suffix = "_update"
    success_url = reverse_lazy('list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('list')

class TodoDetailView(DetailView):
    model = Todo

