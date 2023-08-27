# 
from django.urls import path
from . import views

urlpatterns = [
     path('submit/form/', views.submit_form, name='submit_form'),
      path('send/test/email/', views.send_test_email, name='send_test_email'),
]