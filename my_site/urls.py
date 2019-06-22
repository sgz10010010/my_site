"""my_site URL Configuration

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

from django.contrib import admin
from django.urls import path, include
from home.views import home, contact_me, cv_download

urlpatterns = [
	path('', home, name='home'),
	path('admin/', admin.site.urls),
	path('article/', include('article.urls'), name='article'),
	path('user/', include('user.urls'), name='user'),
	path('user_message/', include('user_message.urls'), name='user_message'),
	path('cv_download/', cv_download, name='cv_download'),
	path('contact_me/', contact_me, name='contact_me'),
]
