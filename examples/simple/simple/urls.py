from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        "^/$", view=TemplateView.as_view(template_name="nine.html"), name="django_nine"
    ),
    # url(r'^admin/', include(admin.site.urls)),
]
