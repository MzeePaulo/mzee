import json

from django.contrib.sites import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect

from promotionapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from promotionapp.forms import ServicesForm,ImageUploadForm
from promotionapp.models import Member, Services,DesignModel


# Create your views here.
def register(request):
    if request.method =='POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                       email=request.POST['email'],
                       username=request.POST['username'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


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

def show(request):
    services = Services.objects.all()
    return render(request, 'show.html', {'services': services})

def delete(request, id):
    services = Services.objects.get(id=id)
    services.delete()
    return redirect('/show')

def edit(request,id):
    service = Services.objects.get(id=id)
    return render(request, 'edit.html', {'service': service})


def update(request,id):
    service = Services.objects.get(id=id)
    form = ServicesForm(request.POST, instance=service)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'service': service})

def upload_image(request):
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/image')
        else:
            form = ImageUploadForm()
        return render(request, 'upload_image.html', {'form': form})


def show_image(request):
    images = DesignModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def imagedelete(request, id):
    image = DesignModel.objects.get(id=id)
    image.delete()
    return redirect('/image')

def pay(request):
    return render(request, 'pay.html')



def token(request):
    consumer_key = 'VjzrDUsm8KAGvXEphTkhdaymwYltbVH3'
    consumer_secret = 'bSnYtig3VCmj1yL1'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")





