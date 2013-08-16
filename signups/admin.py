from django.contrib import admin
import models
from signups.models import Subscriber
from actions import export_as_csv_action



class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name','email','charge_date','charge_id','cust_id','expires_on',)
    actions = [export_as_csv_action("CSV Export", fields=['name','email','charge_date','charge_id','cust_id','expires_on'])]
    class Media:
        css = {'all': ('css/grap_extend.css',)}
        
admin.site.register(Subscriber, SubscriberAdmin)

class ButtonableModelAdmin(admin.ModelAdmin):
   """
   Django snippet # 1936
   Derived from django snippet # 1016
   http://www.djangosnippets.org/snippets/1936/

   A subclass of this admin will let you add buttons (like history) in the
   change view of an entry.

   ex.
   class FooAdmin(ButtonableModelAdmin):
      ...

      def bar(self, obj):
         obj.bar()
      bar.short_description='Example button'

      buttons = [ bar ]

   you can then put the following in your admin/change_form.html template:

      {% block object-tools %}
      {% if change %}{% if not is_popup %}
      <ul class="object-tools">
      {% for button in buttons %}
         <li><a href="{{ button.func_name }}/">{{ button.short_description }}</a></li>
      {% endfor %}
      <li><a href="history/" class="historylink">History</a></li>
      {% if has_absolute_url %}<li><a href="../../../r/{{ content_type_id }}/{{ object_id }}/" class="viewsitelink">View on site</a></li>{% endif%}
      </ul>
      {% endif %}{% endif %}
      {% endblock %}

   """
   buttons=[]

   def change_view(self, request, object_id, extra_context={}):
      extra_context['buttons']=self.buttons
      if '/' in object_id:
         object_id = object_id[:object_id.find('/')]
      return super(ButtonableModelAdmin, self).change_view(request, object_id, extra_context)

   def button_view_dispatcher(self, request, url):
      if url is not None:
         import re
         res=re.match('(.*/)?(?P<id>\d+)/(?P<command>.*)', url)
         if res:
            if res.group('command') in [b.func_name for b in self.buttons]:
               obj = self.model._default_manager.get(pk=res.group('id'))
               getattr(self, res.group('command'))(obj)
               return HttpResponseRedirect(request.META['HTTP_REFERER'])

      return super(ButtonableModelAdmin, self).__call__(request, url)

   def get_urls(self):
       from django.conf.urls.defaults import patterns, url

       def wrap(view):
           def wrapper(*args, **kwargs):
               return self.admin_site.admin_view(view)(*args, **kwargs)
           return update_wrapper(wrapper, view)

       urlpatterns = patterns('',
           url(r'^(.+)/$',
               wrap(self.button_view_dispatcher),)
       ) + super(ButtonableModelAdmin, self).get_urls()
       return urlpatterns