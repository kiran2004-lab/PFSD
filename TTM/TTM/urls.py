from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homePage,name="home"),
    path("Login",views.Login,name="login"),
    path("contact",views.contactpage,name="contact"),
    path("about",views.aboutus,name="about"),
    path("",include("adminapp.urls")),
    path("Register",views.registrationpage,name="register"),
]
