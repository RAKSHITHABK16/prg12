from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('get_demo1/',views.get_demo1,name="get_demo1"),
    path('get_demo2/',views.get_demo2,name="get_demo2"),
    path('post_demo/',views.post_demo,name="post_demo"),
]
