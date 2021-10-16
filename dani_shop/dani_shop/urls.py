import oauth2_provider.views as oauth2_views
from django.contrib import admin
from django.urls import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Documentation of Dani Shop API",
      default_version='v1',
      description="Basic API documentation",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

oauth2_endpoint_views = [
    re_path(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    re_path(r'^access_token/$', oauth2_views.TokenView.as_view(), name="access_token"),
    re_path(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'', include('register_bot.urls')),
    re_path(r'', include('assistance_bot.urls')),
    re_path(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/oauth2/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
