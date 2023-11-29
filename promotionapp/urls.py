import details
from django.contrib import admin
from django.urls import path
from promotionapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio-details'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('team/', views.team, name='team'),
    path('add/', views.add, name='add'),
    path('contact/', views.contact, name='contact'),

]
