from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    # 포스트 목록
    path('', views.index, name='index'),  # 127.0.0.1:8000/blog/
    # 상세 페이지
    path('<int:post_id>/', views.detail, name='detail'),
    # 포스트 작성
    path('post/create/', views.post_create, name='post_create'),
    # 카테고리
    path('category/<str:slug>/', views.category_page, name='category_page'),
]
