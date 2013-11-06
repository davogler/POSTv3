from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject


def site(request):
    '''this, along with
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        "module.context_processors.site",
        ....
    )
    in settings file, will give you {{ site.domain }} to use in this app's templates.'''
    return {
        'site': SimpleLazyObject(lambda: get_current_site(request)),
    }