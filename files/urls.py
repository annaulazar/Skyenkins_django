from django.urls import path
from django.views.generic import TemplateView

from files.apps import FilesConfig
from files.views import FileListView

app_name = FilesConfig.name

urlpatterns = [
    # path('/', FileListView.as_view(), name='list'),
    path('', TemplateView.as_view(template_name='files/home.html'), name='home'),

]