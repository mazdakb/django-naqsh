from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.generic import RedirectView

from rest_framework.reverse import reverse_lazy
from rest_framework.routers import APIRootView

urlpatterns = [
    {%- if cookiecutter.use_grappelli == "y" %}
    # Django Grappelli
    path("grappelli/", include("grappelli.urls")),
    {%- endif %}
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API Root View Session Auth
    path("root-view-auth", include("rest_framework.urls", namespace="rest_framework")),
    # API V1
    path(
        "v1/",
        include(
            (
                [
                    # TODO: custom urls includes go here
                    # === root view
                    path("", APIRootView.as_view(), name="root")
                ],
                "{{cookiecutter.project_slug}}",
            ),
            namespace="v1",
        ),
    ),
    # Service Root View
    path("", RedirectView.as_view(url=reverse_lazy("v1:root"), permanent=False)),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
