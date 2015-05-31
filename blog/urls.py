from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$',views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail),
    url(r'^post_new/$',views.post_new),
    url(r'^post_draft/$',views.post_draft,name="post_draft"),
    url(r'^post/(?P<pk>[0-9]+)/edit$',views.post_edit,name="post_edit"),
    url(r'^post/(?P<pk>[0-9]+)/publish$',views.post_publish,name="post_publish"),
    url(r'^post/(?P<pk>[0-9]+)/remove$',views.post_remove,name="post_remove"),
    

    ]