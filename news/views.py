from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
# from django.views.decorators.csrf import csrf_protect
from django import forms

from .models import Article, Comment

# Create your views here.
def index(request):
    TIMES = 2
    return HttpResponse("Hello! " * TIMES)

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year':year,'article_list':a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year,pub_date__month=month)
    context = {'year':year,'month':month,'article_list':a_list}
    return render(request, 'news/month_archive.html',context)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols':60,'rows':3})
        }

# @csrf_protect
def article_detail(request, year, month, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.article = article
            post.timestamp = timezone.now()
            post.save()
        return HttpResponseRedirect(reverse('news:detail',args=(year,month,pk,)))
    else:
        c_list = Comment.objects.filter(article=article).order_by('-timestamp')
        form = CommentForm()
        context = {'year':year,'month':month,'article':article,'comment_list':c_list,'form':form}
        return render(request, 'news/article_detail.html',context)