"""app views."""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


def index_view(request):
    return render(request, 'index.html')


def filepond_view(request):
    return render(request, 'filepond.html')


@csrf_exempt
def filepond_process_api(request):
    """upload files."""
    return JsonResponse({'ok': 'ok'})


@csrf_exempt
def filepond_revert_api(request):
    """revert upload."""
    return JsonResponse({'ok': 'ok'})


@csrf_exempt
def filepond_restore_api(request):
    return JsonResponse({'ok': 'ok'})


@csrf_exempt
def filepond_load_api(request):
    return JsonResponse({'ok': 'ok'})


@csrf_exempt
def filepond_fetch_api(request):
    return JsonResponse({'ok': 'ok'})
