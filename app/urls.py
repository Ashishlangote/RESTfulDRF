from django.urls import path
from . import views

urlpatterns = [
    path('posts_for_current_user/',views.ListPostsAuthor.as_view(),name='posts_for_current_user'),
    path('posts_for_username/<username>/',views.ListPostsForAuthorUsername.as_view(),name='posts_for_username'),
    path('posts_for/',views.ListPostsForAuthorUsernameUsingQueryParameter.as_view(),name='posts_for'),
    path('homepage/',views.homepage,name="home_page"),
]
    # path('',views.PostListView.as_view(),name="post-list"),
    # path('create/',views.PostCreateView.as_view(),name="post-create"),
    # path('<int:pk>',views.PostDetailView.as_view(),name="post-detail"),
    # path('update/<int:pk>',views.PostUpdateView.as_view(),name="post-update"),
    # path('delete/<int:pk>',views.PostDeleteView.as_view(),name="post-delete"),