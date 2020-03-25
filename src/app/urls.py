from django.urls import path

from . import views

urlpatterns = [
    path('filepond/', views.filepond_view),
]
