from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView


 
urlpatterns = [
    path("", include("hotdogger.urls")),
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html")),
    path("__reload__/", include("django_browser_reload.urls")),

]

