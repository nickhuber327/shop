from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from shop.models import Item

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Item.objects.all().order_by("-date") [:25], template_name="shop/index.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Item, template_name = 'shop/item.html'))
]
