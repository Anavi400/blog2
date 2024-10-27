from django.urls import path
from .views import PostListView, PostDetailView
from .views import PostCreateView, PostDeleteView, PostUpdateView
from .views import FirstPageView
from .views import AddCommentView


urlpatterns = [ 
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("", FirstPageView.as_view, name= "firstpage"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment')
]
#  path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
# 