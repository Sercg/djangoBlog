from django.shortcuts import render, reverse, redirect,HttpResponse,get_object_or_404
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def articles(request):
    keyword = request.GET.get("keyword")
    if  not keyword:
        articles = Article.objects.all()
        context={
            "articles":articles
        }
        return render(request,"articles.html",context)
    else:
        articles = Article.objects.filter(content__contains = keyword)
        context={
            "articles":articles
        }
        return render(request,"articles.html",context)


def index(request):

    return render(request,"index.html")

def about(request):

    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article successfully added")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):   
    #article=Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)

    comments=article.comments.all()

    return render(request,"detail.html",{"article":article, "comments":comments})

@login_required(login_url = "user:login")
def edit(request,id):
    article= get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article successfully updated")
        return redirect("article:dashboard")
    else:
        return render(request,"edit.html",{"form":form})
    
    
@login_required(login_url = "user:login")
def delete(request,id):
    article= get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Article successfully deleted")
    return redirect("article:dashboard")


def addComment(request,id):
    article =get_object_or_404(Article,id=id)

    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        comment=Comment(comment_author=comment_author,comment_content=comment_content)
        comment.article=article
        comment.save()
        messages.success(request,"Your comment is successfully added")
    # return redirect("detail",str(id)) it works
    return redirect(reverse("article:detail",kwargs={"id":id}))



