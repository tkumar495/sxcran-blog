"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from users import views as user_views
app_name = 'users'
urlpatterns = [
    path('admin/', admin.site.urls),
	path('',user_views.home, name="home"),
	path('signup/', user_views.signup, name="signup"),
	path('login/',user_views.login, name="login"),
	path('makepost/', user_views.create_posts, name="makepost"),
	path('error/',user_views.error, name="error"),
	path('success/', user_views.success,name="success"),
	path('dashboard/',user_views.dashboard, name="dashboard"),
	path('profile/', user_views.profile, name="profile"),
	path('logout/', user_views.logout, name="logout"),
	path('<path:slug>', user_views.default, name="default"),
]
urlpatterns += staticfiles_urlpatterns()