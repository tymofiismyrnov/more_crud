from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Contractor
from django.urls import reverse_lazy

'''Project classes'''


class Index(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name_suffix = '_update_form'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'accounts/project_delete.html'
    success_url = "/"


'''Contractor related classes'''


class ContractorCreateView(CreateView):
    model = Contractor
    fields = ['name', 'last_name', 'email', 'project']


class ContractorDetailView(DetailView):
    model = Contractor


class ContractorUpdateView(UpdateView):
    model = Contractor
    template_name = 'accounts/contractor_update.html'
    fields = ['name', 'last_name', 'email', 'project']


class ContractorDeleteView(DeleteView):
    model = Contractor
    template_name = 'accounts/contractor_delete.html'
    success_url = "/"
