from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='upload_form.html'),name='filehome'),
    path('upload',views.create_post,name='upload')
]
