"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from article.views import RSSFeed

urlpatterns = [

	# url(r'^$', 'article.views.home'),
	# url(r'^(?P<my_args>\d+)/$', 'article.views.detail'),
	# url(r'^test/$', 'article.views.test'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'article.views.home', name='home'),
	url(r'^page/(?P<id>\d+)/$', 'article.views.page', name='page'),
	url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
	url(r'^archives/$', 'article.views.archives', name='archives'),
	url(r'^tags/$', 'article.views.tags', name='tags'),
	url(r'^about/$', 'article.views.about', name='about'),
	url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name='search_tag'),
	url(r'^search/$', 'article.views.blog_search', name='search'),
	url(r'^feed/$', RSSFeed(), name="RSS"),
	url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),
]
