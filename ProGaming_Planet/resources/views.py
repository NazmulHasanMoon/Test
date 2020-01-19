from django.shortcuts import render

def basic(request):
    return render(request, 'resources/basic.html')

def programming_language(request):
    return render(request, 'resources/programming_language.html')

def index(request):
    return render(request, 'index.html')

def sort_search(request):
    return render(request, 'resources/sort_search.html')

def ds(request):
    return render(request, 'resources/ds.html')

