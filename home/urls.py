from django.urls import path
from . import views
'''from django.conf import settings
from django.conf.urls.static import static'''
from home.views import index, ContactView

urlpatterns = [
    path('', index.as_view(), name='home'), 
    path('contact/', ContactView.as_view(), name='contact'),
    
]
'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''