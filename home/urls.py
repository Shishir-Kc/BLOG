from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
        path('',views.home,name="home"),
        path('user/upload',views.upload_content,name='content_upload'),
        path('api/user/',views.raw_data),
        path('api/login/',views.login_user),
        path('api/logout/',views.Logout_user),
        path('api/upload/content/',views.User_content_upload),
        path('api/content/',views.User_feed),

]
