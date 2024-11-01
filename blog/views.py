from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseNotAllowed
# Create your views here.


class PostListView(ListView):
    model = Post 
    template_name = "home.html" 

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    fields = ["title", "body", "author"] 
    success_url = reverse_lazy("post_list") 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    template_name = "post_delete.html"
    model = Post
    success_url = reverse_lazy("post_list") 

class PostUpdateView(UpdateView):
    template_name = "post_update.html"
    model = Post
    fields = ["title", "body"]
    success_url = reverse_lazy("post_list") 


class FirstPageView(TemplateView):
    template_name = "registro/firstpage.html"



class AddCommentView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return redirect('post_detail', pk=self.object.pk).url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)  
        

def my_view(request, post_id):
        if request.method == 'POST':
            return HttpResponse('Solicitud POST exitosa.')
        else:
            return HttpResponseNotAllowed(['POST'])