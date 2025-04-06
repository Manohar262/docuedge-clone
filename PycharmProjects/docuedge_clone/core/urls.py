from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('upload/', views.upload_document),
    path('documents/', views.list_documents),
    path('portal/', views.document_portal, name='document_portal'),
]