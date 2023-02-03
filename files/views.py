from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import FileUploadForm
from .models import File, Logs


class FilesListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = 'files/list_files.html'

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)


class AddFileView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = FileUploadForm
    template_name = 'files/add_file.html'
    success_url = reverse_lazy('files:home')
    success_message = 'Файл успешно добавлен!'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = self.request.user
            file.save()

        return redirect(self.success_url)


class DetailFileView(LoginRequiredMixin, DetailView):
    template_name = 'files/detail_info.html'

    def get_object(self, *args, **kwargs):
        try:
            return Logs.objects.get(file_id=self.kwargs['pk'])
        except:
            return None


class UpdateFileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = File
    form_class = FileUploadForm
    template_name = 'files/update_file.html'
    success_url = reverse_lazy('files:home')
    success_message = 'Файл успешно обновлен!'

    def post(self, request, *args, **kwargs):
        file = File.objects.get(id=self.kwargs['pk'])
        file.file.delete()
        super().post(request, *args, **kwargs)

        if self.form_valid:
            self.object.status = File.UPDATED
            self.object.save()

        return redirect(self.success_url)


class DeleteFileView(SuccessMessageMixin, View):
    model = File
    success_url = reverse_lazy('files:home')
    success_message = 'Файл удален!'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        file = File.objects.get(id=self.kwargs['pk'])
        file.delete()
        return redirect(self.success_url)

