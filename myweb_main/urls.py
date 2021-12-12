from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('post', views.post_page, name='post'),
    path('reg', views.reg_page, name='reg'),
    path('auth', views.auth, name='auth')
]

