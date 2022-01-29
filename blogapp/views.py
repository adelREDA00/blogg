from django.db.models import fields
from django.http.response import ResponseHeaders
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect , JsonResponse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Create your views here.

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked =True
    
    toto_likes =  post.likes.all().count()

    data = {
        'value': liked,
        'likes': toto_likes,
    }
    return JsonResponse(data , safe=False)
  



def index(request):
    return render(request,"index.html")

class HomeView(ListView):
    model = Post
    ordering=['-post_date']
    template_name = 'home.html'
    cats = Category.objects.all()
    
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
        
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked= True
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context

    

class AddpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'

class UpdatePostViwe(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url =reverse_lazy('home')

class AddcategoryView(CreateView):
    model = Category
    template_name = 'addCategory.html'
    fields = '__all__'

def CategoryView(request,cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request , "category.html",{'cats':cats.title().replace('-',' ') , 'category_post': category_post})