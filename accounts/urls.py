from django.conf.urls import include, url
from .views import SettingsView

urlpatterns = [
    # Examples:
    # url(r'^$', 'builderdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', SettingsView.as_view(), name='accounts_index'),

]
