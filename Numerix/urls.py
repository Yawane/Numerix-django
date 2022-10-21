from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import app
from Numerix import settings
from app.views import index

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('project/', include('app.urls')),
    path('user/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
