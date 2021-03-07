from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('xyz/<int:id>',views.xyz,name='xyz'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)