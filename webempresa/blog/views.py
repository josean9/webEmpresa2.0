from django.shortcuts import render
def blog(request):
 return render(request, "blog/blog.html")
blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path('', views.blog, name="blog"),
]
webempresa/urls.py
urlpatterns = [
 path('', include('core.urls')),
 path('blog/', include('blog.urls')),
 path('services/', include('services.urls')),
 p