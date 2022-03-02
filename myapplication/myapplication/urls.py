"""myapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.signup),
    path("signup/", views.usersignup),
    path("menu/", views.menupage),
    path("loginpage/", views.loginpage),
    path("home/", views.log),
    path("logout/", views.log_out),
    path("createuser/", views.creuser),
    path("create_user/", views.usercreate),
    path("viewuser", views.userview),
    path('user-edit/<int:id>',views.useredit),
    path('userupdate/<int:id>',views.userupdate),
    path('user-delete/<int:id>',views.userdelete),
]
