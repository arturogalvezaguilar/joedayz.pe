from django.shortcuts import render

def handler404(request):
    return render(request, 'errores/404.html')


def handler500(request):
    return render(request, 'errores/500.html')
