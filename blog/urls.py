from django.urls import path
from .views import CrearPost, PostList, VerPost
from blog import views

app_name = 'blog'

urlpatterns =[ 
    path('post', PostList.as_view(), name='posts'),
    path('post_detail/<int:pk>/', VerPost.as_view(), name="post_detail"),
    #path('posteos', views.posteo, name='posteos'),
    path('crear_post', CrearPost.as_view(), name='crear_post'),
    path('post_detail/<int:pk>/addComment', views.addComment, name='add_comment'),

]