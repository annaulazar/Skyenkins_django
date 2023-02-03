from django.urls import path
from django.views.generic import TemplateView

from files.apps import FilesConfig
from files.views import FilesListView, AddFileView, DeleteFileView, UpdateFileView, DetailFileView

app_name = FilesConfig.name

urlpatterns = [
    path('', FilesListView.as_view(), name='home'),
    path('add_file/', AddFileView.as_view(), name='add'),
    path('<int:pk>/', DetailFileView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateFileView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteFileView.as_view(), name='delete'),

]