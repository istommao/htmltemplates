from django.urls import path

from . import views

urlpatterns = [
    path('view/filepond/', views.filepond_view),
    path('api/filepond/process', views.filepond_process_api),
    path('api/filepond/revert', views.filepond_revert_api),
    path('api/filepond/restore', views.filepond_restore_api),
    path('api/filepond/load', views.filepond_load_api),
    path('api/filepond/fetch', views.filepond_fetch_api)
]
