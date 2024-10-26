from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    template_name = "registration/signup.html" 
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')

def FirstPage(request):
    return render(request, 'first_page.html')