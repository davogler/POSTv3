from django.contrib import admin
from django import forms
from articles.models import Article

class ArticleAdminForm(forms.ModelForm):
	
    class Meta:
        model = Article
	    
class ArticleAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title','author','pub_date','status',)
    form = ArticleAdminForm
	
	
	
admin.site.register(Article, ArticleAdmin)