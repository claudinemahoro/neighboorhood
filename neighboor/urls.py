from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^all-hoods', views.hoods, name='hood'),
    url(r'new-hood/', views.create_hood, name='new-hood'),
    url(r'^comment/(\d+)', views.add_comment, name='comment'),
    url(r'^neighborhood/(\d+)',views.hood_details, name='details'),
    url(r'^business/(\d+)',views.bus_details, name='details1'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)