from django.shortcuts import render

def index(request):
    return render(request, 'app_datas_regulatorias/index.html')

def analytics(request):
    return render(request, 'app_datas_regulatorias/analytics.html')
