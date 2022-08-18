from django.urls import path
from blogs.views import write_blog, retreive_post,edit_posts, delete_post


urlpatterns = [
    path('write_blogs/', write_blog),
    path('get_posts/', retreive_post),
    path('edit_posts/<int:pk>/', edit_posts),
    path('delete_post/<int:pk>/', delete_post),

]
