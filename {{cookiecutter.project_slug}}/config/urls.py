from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views import defaults as default_views
from django.urls import path

from rest_framework.reverse import reverse_lazy
from rest_framework.routers import APIRootView

urlpatterns = [
    {% if cookiecutter.use_grappelli == "y" -%}
    # Django Grappelli
    path('grappelli/', include('grappelli.urls')),
    {%- endif %}
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    url(settings.ADMIN_URL, admin.site.urls),

    # API Root View Session Auth
    url(r'^root-view-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API V1
    url(r'^v1/', include(([

        # TODO: custom urls includes go here

        # === root view
        url(r'^$', APIRootView.as_view(), name='root'),

    ], '{{cookiecutter.project_slug}}-api-v1'), namespace='v1')),

    # Service Root View
    url(r'^$', RedirectView.as_view(url=reverse_lazy('v1:root'), permanent=False)),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
