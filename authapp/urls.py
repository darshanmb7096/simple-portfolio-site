
from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('about',views.about,name="about"),
    path('resume',views.resume,name="resume"),
    path('hero',views.hero,name="hero"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('projectdetails',views.projectdetails,name="projectdetails"),
    path('signin',views.signin,name="signin"),
    path('login',views.user_login,name="login"),
    path('signup',views.signin,name="signup"),
    path('logout',views.handleLogout,name="handleLogout"),
]