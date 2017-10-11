from django.conf.urls import url

from .views import ShortenURLView, OriginalUrlView

urlpatterns = [
    url(r'^$', ShortenURLView.as_view(), name="add_url"),
    url(r'^(?P<hashval>[a-zA-Z0-9]+)$', OriginalUrlView.as_view(), name="get_url"),
]