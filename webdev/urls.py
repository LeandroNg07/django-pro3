
from django.urls import path
from django.contrib import admin
from contatos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowContacts, name="home"),
    path('add/', views.AddContact),
    path('detail/<int:detail_id>/', views.ContactDetailView, name="detail"),
    path('edit/<int:detail_id>/', views.ContactDetailEdit, name="edit"),
    path('delete/<int:detail_id>/', views.ContactDelete, name="delete"),
]