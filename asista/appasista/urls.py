from django.conf.urls import url
from appasista import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name = "home"),
    url(r'^first$', views.first, name = "first"),
    url(r'^manufacturer$', views.manufacturer, name = "manufacturer"),
    url(r'^funder$', views.funder, name = "funder"),
    url(r'^customer$',views.customer,name="customer"),
    url(r'^added_products$',views.added_products,name="added_products"),
    url(r'^home_h$',views.home_h,name="home_h"),
    url(r'^launch$',views.launch,name="launch"),
    url(r'^link/([0-9]+)/$',views.link,name="link"),
    url(r'^flink/([0-9]+)/$',views.flink,name="flink"),
    url(r'^login/$', auth_views.login,name = 'login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name = 'logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^Saved/$', views.Saved, name = 'Saved'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^manufacturer_addproduct$', views.manufacturer_addproduct, name = "manufact_addproduct"),
]
