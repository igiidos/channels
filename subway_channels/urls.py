"""subway_channels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat_app.urls')),
    path('accounts/', include('accounts.urls')),
]


from django.views import static
static_list = [
    (settings.STATIC_URL, settings.STATIC_ROOT),
    (settings.MEDIA_URL, settings.MEDIA_ROOT),
]
for (prefix_url, root) in static_list:
    if '://' not in prefix_url: # 외부 서버에서 서빙하는 것이 아니라면
        prefix_url = prefix_url.lstrip('/')
        url_pattern = r'^' + prefix_url + r'(?P<path>.+)'
        pattern = url(url_pattern, static.serve, kwargs={'document_root': root})
        urlpatterns.append(pattern)