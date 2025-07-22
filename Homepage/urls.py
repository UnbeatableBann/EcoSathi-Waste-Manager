from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings        #in urls.py homepage
from . import views
urlpatterns = [

path('', views.home, name='home'),
path('login', views.login, name='login'),
path('signup', views.signup, name='signup'),
path('login_view', views.login_view, name='login_view'),
path('home', views.home, name='home'),
path('create_account', views.create_account, name='create_account'),
path('forgotpassword', views.forgotpassword, name='forgotpassword'),

#URLs for endusers
path('complain_view',views.complain_view,name='complain'),
#this added today
path('map_view', views.map_view, name='map_view'),
path('get_nearby_dustbins', views.get_nearby_dustbins, name='get_nearby_dustbins'),


#URLs for business
#path('complain_view',views.complain_view,name='complain'),
path('pickup_booking/', views.pickup_booking_view , name='pickup_booking'),
path('learn_more', views.learn_more, name='learn_more'),
#path('complain_table/', views.complain_table, name='complain_table'),


path('cancel_complaint/<int:complaint_id>/', views.cancel_complaint_view, name='cancel_complaint'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)