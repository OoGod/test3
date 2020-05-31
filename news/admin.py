from django.contrib import admin
from . import models

# Register your models here.
class ArticleInline(admin.TabularInline):
	model = models.Article
	extra = 0

class ReporterAdmin(admin.ModelAdmin):
	inlines = [ArticleInline]

class CommentInline(admin.TabularInline):
	model = models.Comment
	extra = 3

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['headline','content','pub_date']
	inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
	list_display = ['text','article','timestamp']
	list_filter = ['timestamp']
	search_fields = ['text']

admin.site.register(models.Reporter,ReporterAdmin)
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment,CommentAdmin)