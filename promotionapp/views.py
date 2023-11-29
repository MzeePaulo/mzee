from django.shortcuts import render, redirect
from promotionapp.forms import ServicesForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def add(request):
    if request.method=='POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ServicesForm()
        return render(request, 'addservices.html', {'form':form})




