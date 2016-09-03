
from django.conf.urls import url
from django.contrib import admin
from .views import (
    hackathon_home,
    hackathon_sign_up,
    hackathon_log_in,
    hackathon_log_out,
    hackathon_hdc
    ) 

urlpatterns = [
    url(r'^$', hackathon_home), 
    url(r'^home/$', hackathon_home),
    url(r'^log-in/$', hackathon_log_in),
   	url(r'^log-out/$', hackathon_log_out),
    url(r'^sign-up/$', hackathon_sign_up),
    url(r'^mi-impacto/$', hackathon_hdc),

]
