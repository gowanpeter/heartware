
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from ware import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home$', 'ware.views.home', name='home'),
    url(r'^glaze$', 'ware.views.GlazeView', name='glaze'),
    url(r'^documentation$', 'ware.views.DocumentationView', name='documentation',),
     url(r'^condition$', 'ware.views.ConditionView', name='condition',),
     url(r'^exhibition$', 'ware.views.ExhibitionView', name='exhibition',),
     url(r'^hline$', 'ware.views.HeathLineLookupView', name='hline',),
     url(r'^logo$', 'ware.views.LogoView', name='logo',),
     url(r'^maker$', 'ware.views.MakerLookupView', name='maker',),
     url(r'^material$', 'ware.views.MaterialLookupView', name='material',),
     url(r'^method$', 'ware.views.MethodLookupView', name='method',),
     url(r'^pub$', 'ware.views.PublicationView', name='pub',),
     url(r'^setc$', 'ware.views.SetCollectionView', name='set',),
     )




    #src/kk
 #   url(r'^ware/', include('ware.urls', namespace='ware', app_name='kk')),
 #   url(r'^$',ware.views.kk_directory, name='kk')


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
