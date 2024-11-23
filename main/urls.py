from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Define the URL patterns for the app. The '' path maps to the 'home' view
urlpatterns =[
    path('',views.home,name='home'),
    path('student/slogin',views.slogin,name='slogin'),
    path('tutor/tutorlogin',views.tutorlogin,name='tutorlogin'),
    path('message',views.message,name='message'),
    path('select_recipient/', views.select_recipient, name='select_recipient'),
    path('message/<int:recipient_id>/', views.message, name='message'),

     

]
#If DEBUG is True, serve media files (like images) during development
#by appending a route to the urlpatterns that maps MEDIA_URL to MEDIA_ROOT locally
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
