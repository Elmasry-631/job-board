from django.contrib.auth.urls import urlpatterns
from django.urls import path,include
from . import views

app_name = 'job'

urlpatterns =[

    path('',views.job_list),
    path('<str:slug>',views.job_detail , name='job_detail'),

]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
