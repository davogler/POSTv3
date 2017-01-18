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


def banner(context, request):
    '''a view for snagging featured entries for display on front page or sidebar.
    This view requires the request object to be passed to it in order to check the user's authentication status.
    For example, the templatetag {% featuredlist request %} is required in the template.
    Authenticated users may see unpublished entries, anonymous users will not.'''
    pubset = Issue.published.exclude(pub_date__gte=datetime.datetime.now())
    if request.user.is_authenticated():
        unpubset = Issue.draft.exclude(pub_date__gte=datetime.datetime.now())
    else:
        unpubset = Issue.published.exclude(pub_date__gte=datetime.datetime.now())
    queryset = (pubset | unpubset)
    user = request.user
    latest = Issue.objects.filter(status=1)[:1]

    context_object_name = 'issue'
    return {'latest': latest, 'user': user, 'request': request}

register.inclusion_tag('banner.html', takes_context=True)(banner)


def admin_links(request):
    previews = Article.objects.filter(status=2)
    return {'previews': previews}

register.inclusion_tag('admin_links.html')(admin_links)


def back_issues(request):
    backissueset = Issue.objects.filter(for_sale=True)
    return {'backissueset': backissueset}

register.inclusion_tag('back_issues.html')(back_issues)


def article_popular_teasers(request):
    artset = Article.objects.filter(featured=1).filter(popular=1).filter(status=1)[:6]
    return {'artset': artset}

register.inclusion_tag('articles/issue_teaser_list.html')(article_popular_teasers)


def issue_slider(request):
    issueset = Issue.objects.filter(status=1)
    return {'issueset': issueset}

register.inclusion_tag('articles/issue_slider.html')(issue_slider)
