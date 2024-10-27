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

class LogOutView(CreateView):
    template_name = "registration/logout.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('firstpage')

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Post, Comment

# def add_comment(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == "POST":
#         text = request.POST.get('comment')
#         Comment.objects.create(post=post, text=text, author=request.user)
#         return redirect('post_detail', post_id=post_id)
#     return render(request, 'add_comment.html', {'post': post})