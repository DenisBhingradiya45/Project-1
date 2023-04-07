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
    path('DeleteBlog/<int:id>/', DeleteBlog, name="DeleteBlog"),
    path('BlogDetails/<int:id>/', BlogDetails, name="BlogDetails"),
    path('UserBlog/', UserBlog, name='UserBlog')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


print("",static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))