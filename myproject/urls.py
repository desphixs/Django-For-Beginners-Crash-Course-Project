"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="my_home_page"),
    path("about/us/visit/come-today/", views.about, name="about_page"),
    path("contact/", views.contact),
    path("pricing/", views.pricing),
    path("post-detail/<post_id>/", views.post_detail, name="post_detail"),
    path("create-post/", views.create_post, name="create_post"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("register/", views.register_view, name="register_view"),
]
