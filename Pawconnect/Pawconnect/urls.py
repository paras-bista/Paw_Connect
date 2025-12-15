from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views 
  # import base view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(f'{settings.ADMIN_URL}/', admin.site.urls),  # Custom admin URL for security
    path('', accounts_views.base, name='home'),          # ← home page at /
    path('accounts/', include('accounts.urls')),
    path('donate/', include('donation.urls')),  # ✅ new
    path('rescue/', include('rescue.urls')),  # ✅ new
    path('contact/', include('contact.urls')),  # ✅ new
    path('adopt/', include('adopt.urls')),  # ✅ new
    path('volunteer/', include('volunteer.urls')),
    path('api/', include('backend.urls')),  # ✅ new
    # path('auth/', include('social_django.urls', namespace='social')),  # Google OAuth - disabled for now
    # path('news/', include('newsfeed.urls')),  # ✅ new
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
