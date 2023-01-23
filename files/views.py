from django.shortcuts import render
from django.views.generic import ListView

class FileListView(ListView):
    template_name = 'users/base.html'
    queryset = None
