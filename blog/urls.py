from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls.py')),
    path('blog/', include('blog.urls.py')),
    path('accounts/', include('accounts.urls.py')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)