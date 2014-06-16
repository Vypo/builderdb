# Unlike the rest of BuilderDB, this file is released under the following
# terms:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views
from django.contrib.sitemaps import FlatPageSitemap
from builders.sitemap import BuilderSitemap, ReviewSitemap

sitemaps = {
    'flatpages': FlatPageSitemap,
    'builders': BuilderSitemap,
    'reviews': ReviewSitemap,
}

urlpatterns = [
    # Examples:
    # url(r'^$', 'builderdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^pages/privacy/$', views.flatpage, {'url': '/pages/privacy/'}, name='flat_privacy'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/avatar/', include('avatar.urls')),
    url(r'^', include('builders.urls')),
]

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT) + urlpatterns
