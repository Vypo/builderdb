from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'builderdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/avatar/', include('avatar.urls')),
    url(r'^', include('builders.urls')),
]

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT) + urlpatterns
