from django.contrib import admin
from django import forms
from articles.models import Article, Author, Sponsor, Photog, Image, Illus, Issue

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class ArticleAdminForm(forms.ModelForm):
    
    class Meta:
        model = Article
	    
class ArticleAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title', 'pub_date','status','featured', 'sponsor')
    list_editable = ('status','featured',)
    
    inlines = [ ImageInline, ]
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)



class AuthorAdminForm(forms.ModelForm):
	
    class Meta:
        model = Author
	    
class AuthorAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    form = AuthorAdminForm	

admin.site.register(Author, AuthorAdmin)

class PhotogAdminForm(forms.ModelForm):
	
    class Meta:
        model = Photog
	    
class PhotogAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    form = PhotogAdminForm	

admin.site.register(Photog, PhotogAdmin)

class IllusAdminForm(forms.ModelForm):
	
    class Meta:
        model = Illus
	    
class IllusAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    form = IllusAdminForm	

admin.site.register(Illus, IllusAdmin)

class SponsorAdminForm(forms.ModelForm):
	
    class Meta:
        model = Sponsor
	    
class SponsorAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    form = SponsorAdminForm
    		
admin.site.register(Sponsor, SponsorAdmin)

class IssueAdminForm(forms.ModelForm):
	
    class Meta:
        model = Issue
	    
class IssueAdmin(admin.ModelAdmin): 
    list_display = ('month', 'thumb')
    form = IssueAdminForm	

admin.site.register(Issue, IssueAdmin)