from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
def home(request):
    dict={'name':"योगी युञ्जीत सततमात्मानं रहसि स्थित: |एकाकी यतचित्तात्मा निराशीरपरिग्रह: || 10||",'name1':"Chapter 6 Dhyana yoga",'name2':"Those who seek the state of Yogi should reside in seclusion, constantly engaged in meditation with a controlled mind and body, getting rid of desires and possessions for enjoyment."}
    return render(request,'home.html',context=dict)
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'