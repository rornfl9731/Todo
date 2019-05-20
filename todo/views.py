from django.shortcuts import render,render_to_response,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from todo.forms import PostForm
from .models import Todo
import datetime
# Create your views here.

class TodoListView(ListView):
    model = Todo
    paginate_by = 10

    # def get_ordering(self):
    #     ordering = self.request.GET.get('ordering', 'priority')
    #     # validate ordering here
    #     return ordering

    def get_queryset(self):
        return Todo.objects.order_by('priority')



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


def cross(request,pk):
    content = Todo.objects.get(pk=pk)
    content.success ^= True
    content.save()

    return redirect('list')


class TodoSuccessListView(ListView):
    model = Todo
    paginate_by = 10
    template_name_suffix = "_success_list"

    def get_queryset(self):

        return Todo.objects.filter(success = True)



