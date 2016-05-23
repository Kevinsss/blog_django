# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100, verbose_name='标题')  # blog title
	category = models.CharField(max_length=50, blank=True, verbose_name='类别')  # blog tag
	date_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
	content = models.TextField(blank=True, null=True, verbose_name='内容')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id': self.id})
		return "http://127.0.0.1:8000%s" % path

	class Meta:
		ordering = ['-date_time']
		verbose_name = '文章'
		verbose_name_plural = '文章'
