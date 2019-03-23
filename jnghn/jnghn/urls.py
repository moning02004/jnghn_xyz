from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app_main.urls')),
    path('user/', include('app_user.urls')),
    path('plan/', include('app_plan.urls')),
    path('material/', include('app_material.urls')),
    path('coffee/', include('app_coffee.urls')),
    path('review/', include('app_review.urls')),
    path('administrator/', include('app_admin.urls')),
    path('notice/', include('app_notice.urls')),
    path('freetalk/', include('app_freetalk.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



