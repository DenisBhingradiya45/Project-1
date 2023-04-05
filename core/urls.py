from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('SignUp/', SignUp, name="SignUp"),
    path('SignIn/', SignIn, name="SignIn"),
    path('LogOut/', LogOut, name="LogOut"),
    path('home/', home, name="home"),
    path('about/', about_us, name="about_us"),
    path('BlogDetails/', BlogDetails, name="BlogDetails"),
    path('AddBlog/', AddBlog, name="AddBlog"),
    path('profile/', profile, name="profile"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


print("",static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))