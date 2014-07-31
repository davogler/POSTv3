from django.template import Library
from django import template
from django.db.models import get_model
from articles.models import Article, Issue
from django.contrib.auth.decorators import login_required


from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
import datetime
     
register = Library()
register = template.Library()


def banner(request):
	'''a view for snagging featured entries for display on front page or sidebar.  This view requires the request object to be passed to it in order to check the user's authentication status.  For example, the templatetag {% featuredlist request %} is required in the template.  Authenticated users may see unpublished entries, anonymous users will not.'''
	pubset = Article.published.exclude(pub_date__gte=datetime.datetime.now())
	if request.user.is_authenticated():
	    unpubset = Article.draft.exclude(pub_date__gte=datetime.datetime.now())
	else:
	    unpubset = Article.published.exclude(pub_date__gte=datetime.datetime.now())
	queryset = (pubset | unpubset)
	user = request.user
	latest = Article.objects.filter(featured=1).filter(status=1)[:1]
	return {'latest': latest, 'user':user }
	
register.inclusion_tag('banner.html')(banner)


def admin_links(request):
    
    previews = Article.objects.filter(status=2)
    return {'previews': previews}
    
register.inclusion_tag('admin_links.html')(admin_links)

def back_issues(request):
    
    backissueset = Issue.objects.filter(for_sale=True)
    return {'backissueset': backissueset}
    
register.inclusion_tag('back_issues.html')(back_issues)