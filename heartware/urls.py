from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heartware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#urlpatterns = patterns('',
    #url(r'^ware/', include('ware.urls')),
    #url(r'^admin/', include(admin.site.urls)),
#)
