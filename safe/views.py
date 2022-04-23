from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
import base64
from .models import Locker, User

class Signup(View):
    def get(self,request):
        return render(request, 'landing.html')
    def post(self,request):
        if request.POST['name']:
            user=request.POST['name']
            email=request.POST['email']
            pwd=request.POST['pswd']
            if User.objects.filter(email=email):
                return HttpResponse("Email already exists.. Please Login!!!")
            new_entry=User(Name=user, email=email, passwd=pwd)
            new_entry.save()
            request.session['email']=email
        return redirect('PasswordSafe')

class Login(View):
    def get(self,request):
        return render(request, 'landing.html')
    def post(self,request):
        email=request.POST['email']
        pwd=request.POST['pswd']
        if User.objects.filter(email=email) and User.objects.filter(passwd=pwd):
            request.session['email']=email
            return redirect('PasswordSafe')
        messages.error(request, 'Invalid email/password Please try again!!!')
        return redirect('landing')
    
class Safekeeper(View):
    
    def get(self,request):
        em=request.session.get('email')
        data=Locker.objects.filter(email=em).values("domain","username","password")
        resp = []
        for i in range(len(data)):
            resp.append({
                "domain" : data[i]['domain'],
                "username" : data[i]['username'],
                "password" : base64.b64decode(data[i]['password']).decode("ascii"),
            })
        return render(request, 'PassSafe.html', {'data':resp})
    def post(self,request):
        em=request.session.get('email')
        site=request.POST['Domain']
        user=request.POST['Uname']
        pwd=request.POST['password'].encode("ascii")
        encpwd=base64.b64encode(pwd)
        new_entry=Locker(domain=site, username=user, password=encpwd,email=User.objects.get(email=em))
        new_entry.save()
        messages.success(request, 'Changes successfully saved.')
        return redirect('PasswordSafe')