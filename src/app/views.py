from django.shortcuts import render


def filepond_view(request):
    return render(request, 'filepond.html')
