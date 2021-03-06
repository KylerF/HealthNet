"""healthnet_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    url(r'^healthnet/', include('healthnet.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^messages/lookups/',
        include(ajax_select_urls)),
    url(r'^messages/', include('postman.urls')),
    url(r'^admin/', admin.site.urls),
]
