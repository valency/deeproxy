from django.conf.urls import url
from django.views.decorators.cache import cache_page

from deeproxy.views import *

urlpatterns = [
    url(r'html/', cache_page(24 * 3600)(ProxyHtmlView.as_view())),
    url(r'img/', cache_page(24 * 3600)(ProxyImageView.as_view()))
]
