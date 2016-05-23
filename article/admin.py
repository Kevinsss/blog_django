from django.contrib import admin

from article.models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	# fields = ['title', 'content']

	class Media:
		js = ['/js/tinymce/tinymce.min.js', '/js/tinymce/textareas.js']


admin.site.register(Article, ArticleAdmin)
