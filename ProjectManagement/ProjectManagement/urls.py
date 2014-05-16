from django.conf.urls import patterns, include, url
from ProjectsApp.views import *

urlpatterns = patterns('',
	url(r'^task/$', tasks),
    url(r'^addproject/$', create_project),
    url(r'^projects/$', projects),
    url(r'^newtask/$', create_task),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^projects/',include ('ProjectsApp.urls', namespace = 'ProjectManagement')),
    #url(r'^hello/$', new), #Acuerdese, el primer parametro es para la url y el segundo es la vista
)
