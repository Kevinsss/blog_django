# coding: utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from article.models import Article
from django.db.models import Count, Avg
from django.http import Http404


# Create your views here.
def home(request):
	posts = Article.objects.all()
	paginator = Paginator(posts, 3)
	page = request.GET.get('page')

	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.paginator(paginator.num_pages)
	return render(request, 'home.html', {'post_list': post_list})


def page(request, id):
	posts = Article.objects.all()
	paginator = Paginator(posts, 3)
	try:
		post_list = paginator.page(id)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.paginator(paginator.num_pages)
	return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'post.html', {'post': post})


def archives(request):
	try:
		post_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def tags(request):
	try:
		tag_list = Article.objects.values('category').annotate(category_num=Count('category'))
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'tags.html', {'tag_list': tag_list})


def about(request):
	return render(request, 'about.html')


def search_tag(request, tag):
	try:
		post_list = Article.objects.filter(category__iexact=tag)
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'post_list': post_list})


def blog_search(request):
	if 's' in request.GET:
		s = request.GET['s']
		print(s)
		if s is None:
			return render(request, 'home.html')
		else:
			post_list = Article.objects.filter(title__icontains=s)
			if len(post_list) == 0:
				return render(request, 'archives.html', {'post_list': post_list, 'error': True})
			else:
				return render(request, 'archives.html', {'post_list': post_list, 'error': False})

	return redirect('/')


from django.contrib.syndication.views import Feed


class RSSFeed(Feed):
	title = "RSS feed - article"
	link = "feeds/posts/"
	description = "RSS feed - blog posts"

	def items(self):
		return Article.objects.order_by('-date_time')

	def item_title(self, item):
		return item.title

	def item_pubdate(self, item):
		return item.date_time

	def item_description(self, item):
		return item.content
