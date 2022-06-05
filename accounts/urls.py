from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('project/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/<pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<pk>/delete/', views.ProjectDeleteView.as_view(), name="project-delete"),
    path('contractor/new/', views.ContractorCreateView.as_view(), name='contractor-create'),
    path('contractor/<pk>/', views.ContractorDetailView.as_view(), name='contractor-detail'),
    path('contractor/<pk>/update/', views.ContractorUpdateView.as_view(), name='contractor-update'),
    path('contractor/<pk>/delete/', views.ContractorDeleteView.as_view(), name='contractor-delete'),
]
