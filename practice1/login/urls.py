from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login,name='logi'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^home/$',views.home,name='home'),
    url(r'^logout/$',views.logout,name='logo')
    
]