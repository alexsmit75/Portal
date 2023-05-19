from django.urls import path
from django.conf import settings
from django.shortcuts import redirect
from .views import (
    PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView,PostSearch,BaseRegisterView
)
from .views import  CategoryListView, subscribe, unsubscribe
from django.contrib.auth.views import LoginView, LogoutView
from .views import upgrade_me
from .views import IndexView
urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   #path('protected/', ProtectedView.as_view(), name='protected_page'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/',  PostCreateView.as_view(), name='article_add'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('login/',
        LoginView.as_view(template_name='news/login.html'),
        name='login'),
   path('logout/',
        LogoutView.as_view(template_name='news/logout.html'),
        name='logout'),
   path('signup/',
        BaseRegisterView.as_view(template_name='news/signup.html'),
        name='signup'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('', IndexView.as_view()),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]