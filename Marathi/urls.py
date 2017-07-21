from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index, name="index" ),

    url(r'^register/$',views.UserFormView.as_view(), name="reg" ),
    
    url(r'^dashboard/$',views.Admin, name="admin" ),

    url(r'^marathi/add/$',views.CreateMovie.as_view() , name="M-add"),

    url(r'^profile/$',views.Profile, name="profile" ), 

    url(r'^MovieDeatil/$',views.moviedeatil, name="Mdetail" ), 
    
    url(r'^(?P<pk>[0-9]+)/$',views.DetailMovie.as_view(),name="detail"),

    url(r'^Update/(?P<pk>[0-9]+)/$',views.UpdateMovie.as_view(),name="up-movie"),   
    
    url(r'^(?P<pk>[0-9]+)delete/$',views.DeleteMovie.as_view(),name="del-movie"),
   
]
