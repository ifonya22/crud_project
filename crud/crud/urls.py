from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]
urlpatterns += doc_url
