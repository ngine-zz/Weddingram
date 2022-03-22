from content import views
from django.urls import path
from .views import UploadFeed, UploadReply



app_name = 'content'
urlpatterns= [
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('copyright/', views.copyright, name='copyright'),
    path('weddingvows/', views.weddingvows, name='weddingvows'),
    path('location/', views.location, name='location'),
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view())
]