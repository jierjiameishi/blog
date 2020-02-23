from django.urls import path

from . import views

app_name = 'jier'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>', views.detail, name='detail'),
    #     <int:pk> 是 django 路由匹配规则的特殊写法，其作用是从用户访问的 URL 里把匹配到的数字捕获并作为关键字参数传给其对应的视图函数 detail。
    path('archives/<int:year>/<int:month>', views.archive, name='archive'),
    path('category/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>', views.tag, name='tag')
]
