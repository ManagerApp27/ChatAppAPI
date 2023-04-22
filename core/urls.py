from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from contact.urls import router_contact
from message.urls import router_message


urlpatterns = [   
    path('api/', include(router_contact.urls)),
    path('api/', include(router_message.urls)),
    path('api/', include('user.urls')),
    path('api/', include('message.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)