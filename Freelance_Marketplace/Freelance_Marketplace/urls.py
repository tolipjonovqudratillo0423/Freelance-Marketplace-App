from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



# =========================================================
# CORE URLS
# =========================================================

urlpatterns = [
    path('BIG_BROTHER/', admin.site.urls),
]



# =========================================================
# APPS
# =========================================================

urlpatterns += [
    path('auth/', include('apps.users.urls')),
    path('client/', include('apps.projects.urls')),
    path('freelancer/', include('apps.bids.urls')),
    path('common/', include('apps.common.urls')),
]



# =========================================================
# DEBUG TOOLS URLS
# =========================================================

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    
    urlpatterns += [
    # YOUR PATTERNS
        path('api/info/download', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
            path('api/info', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
            path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]