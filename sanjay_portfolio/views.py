from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.views import View


# Create your views here.
class BasePage(View):
    def get(self,request):
        return render(request,'base.html')
class SendMail(View):
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)


        send_mail(subject,message,email,['sanjayp9072@gmail.com'],fail_silently=False)
        return redirect('basepage')
