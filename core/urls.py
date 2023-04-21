from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Home/', Home, name="Home"),
    path('SignUp/', SignUp, name="SignUp"),
    path('SignIn/', SignIn, name="SignIn"),
    path('LogOut/', LogOut, name="LogOut"),
    path('Profile/', Profile, name="Profile"),
    path('AboutUs/', AboutUs, name="AboutUs"),
    path('AddBlog/', AddBlog, name="AddBlog"),
    path('UpdateBlog/<int:pk>/', UpdateBlog, name="UpdateBlog"),
    path('DeleteBlog/<int:pk>/', DeleteBlog, name="DeleteBlog"),
    path('BlogDetails/<int:pk>/', BlogDetails, name="BlogDetails"),
    path('UserBlog/', UserBlog, name='UserBlog'),
    path('LikeBlog/<int:post_id>/', LikeBlog, name='LikeBlog'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# print("",static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
# print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))