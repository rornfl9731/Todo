from django.urls import path
from .views import TodoListView,TodoCreateView,TodoUpdateView,TodoDeleteView,TodoDetailView,cross

urlpatterns =[
    path("",TodoListView.as_view(),name="list"),
    path("add/",TodoCreateView.as_view(),name="add"),
    path("update/<int:pk>",TodoUpdateView.as_view(),name="update"),
    path("delete/<int:pk>",TodoDeleteView.as_view(),name="delete"),
    path("detail/<int:pk>",TodoDetailView.as_view(),name="detail"),
    path("cross/<int:pk>",cross,name="cross")

]