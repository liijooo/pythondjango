"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from books import views
app_name='books'
urlpatterns = [
    # path('', views.home, name='home'),
    path('',views.HomeView.as_view(),name='home'),
    # path('addbook', views.addbook, name='addbook'),
    path('addbook',views.AddbookView.as_view(),name='addbook'),
    # path('viewbook', views.viewbook, name='viewbook'),
    path('viewbook',views.Viewbook.as_view(),name='viewbook'),
    # path('addbook1',views.addbook1,name='addbook1'),
    path('addbook1',views.AddbookView1.as_view(),name='addbook1'),
    # path('bookdetail/<int:i>',views.bookdetail,name='bookdetail'),
    path('bookdetail/<int:i>',views.Bookdetail.as_view(),name='bookdetail'),
    # path('editbook/<int:i>',views.editbook,name='editbook'),
    path('editbook/<int:i>',views.Editbook.as_view(),name='editbook'),
    # path('deletebook/<int:i>',views.deletebook,name='deletebook'),
    path('deletebook/<int:i>',views.Deletebook.as_view(),name='deletebook'),
    # path('searchbook',views.searchbook,name='searchbook'),
    path('searchbook',views.Searchbook.as_view(),name='searchbook'),
    path('user/register/', views.SignupView.as_view(), name='register'),
    path('user/login/', views.SigninView.as_view(), name='login'),
    path('user/logout/', views.SignoutView.as_view(), name='logout'),
]
