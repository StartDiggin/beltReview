from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^addBook$', views.addBook),
    url(r'^create$', views.create),
    url(r'^review/(?P<id>\d+)$', views.review),
    url(r'^usersPage/(?P<id>\d+)$', views.user),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^addReview/(?P<id>\d+)', views.addReview),
]
