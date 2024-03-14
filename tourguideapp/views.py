from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def myweb(request):
    return render(request, 'my web.html')

def about(request):
    return render(request, 'about.html')


def Tables(request):
    return render(request, 'Tables.html')
def form(request):
    return render(request, 'form.html')