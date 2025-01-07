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
    path('library/', views.library, name='library'),
    path('student/studentprof/', views.studentprof, name='studentprof'),
    path('logouta/', views.logouta, name='logouta'),
    path('contactus/', views.contactus, name='contactus'),
    path('showfaq', views.showfaq, name='showfaq'),
    path('addfaq', views.addfaq, name='addfaq'),
    path('faqs/edit/<int:id>/', views.editfaq, name='editfaq'),
    path('faqs/delete/<int:id>/', views.deletefaq, name='deletefaq'),
    path('tests/addtests/', views.addtest, name='addtests'),
    path('tests/delete/<int:id>/', views.deletetest, name='deletetest'),
    path('tests/addquestion/<int:test_id>', views.addquestion, name='addquestion'),
    path('tests/editquestion/<int:id>/<int:test_id>/', views.editquestion, name='editquestion'),
    path('tests/deletequestion/<int:id>/<int:test_id>/', views.deletequestion, name='deletequestion'),
    path('selecttest/', views.selecttest, name='selecttest'),
    path('viewtest/<int:test_id>/', views.viewtest, name='viewtest'),
    path('selecttest2/', views.selecttest2, name='selecttest2'),
    path('answertest/<int:test_id>/', views.answertest, name='answertest'),



]
#If DEBUG is True, serve media files (like images) during development
#by appending a route to the urlpatterns that maps MEDIA_URL to MEDIA_ROOT locally
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
