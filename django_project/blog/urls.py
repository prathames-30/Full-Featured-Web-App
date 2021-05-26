from django.urls import path
from . import views 
from users import views as user_views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    #path('', views.home, name = 'blog-home'),
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),  #pk  = primary key i.e if we go to /post/1(pk = 1) then we go to blog with id 1
    path('post/new/', PostCreateView.as_view(), name = 'post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('register/',user_views.register, name ='register'),
    path('about/', views.about, name = 'blog-about'),

]

#class based views look for naming conditions of form,
#<app>/<model>_<viewtype>.html