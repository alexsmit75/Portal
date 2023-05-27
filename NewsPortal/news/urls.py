from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('news/', PostList.as_view(), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/',  PostCreate.as_view(), name='create_post'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]