from django.contrib import admin
from .models import Todo
# Register your models here.

class todo_admin(admin.ModelAdmin):
    list_display = ('priority','title','content','due_date','success')

admin.site.register(Todo,todo_admin)