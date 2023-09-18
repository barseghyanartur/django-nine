from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # path('', 'simple.views.home', name='home'),
    # path('blog/', include('blog.urls')),
    path(
        "/", view=TemplateView.as_view(template_name="nine.html"), name="django_nine"
    ),
    # path('admin/', include(admin.site.urls)),
]
