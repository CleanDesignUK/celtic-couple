# celtic_couple_blog/urls.py

from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls  # Updated import

from search import views as search_views

urlpatterns = [
    # Django's default admin interface (optional)
    path('django-admin/', admin.site.urls),

    # Wagtail's admin interface
    path('cms/admin/', include(wagtailadmin_urls)),

    # Wagtail's documents
    path('cms/documents/', include(wagtaildocs_urls)),

    # Your custom home page at root
    path('', include('home.urls')),  # Serves '/' URL
    path('gallery/', include('gallery.urls', namespace='gallery')),
    # Your custom pages (About, Contact, Work With Us, etc.)
    path('', include('pages.urls')),  # Serves '/about/', '/contact/', etc.


    # Search functionality
    path('search/', search_views.search, name='search'),

    path('cms/blog/', include('blog.urls', namespace='blog')),  # Blog under /cms/blog/
    path('cms/', include('wagtail.urls')),  # General Wagtail URLs for other content
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files during development
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
