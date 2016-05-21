from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^message$' , views.message , name='message' ) ,
    url(r'^parrot$'  , views.parrot  , name='parrot'  ) ,
    url(r'^$'        , views.index   , name='index'   ) ,
]
