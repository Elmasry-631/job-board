from django.contrib.auth.urls import urlpatterns
from django.urls import path,include
from . import views
from . import api
app_name = 'job'

urlpatterns =[

    path('',views.job_list, name='job_list'),
    path('add',views.add_job , name='add_job'),
    path('<str:slug>',views.job_detail , name='job_detail'),

    path('api/jobs/', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),


    path('api/v2/jobs/', api.Joblistcbv.as_view(), name='job_list_cbv'),
    path('api/v2/jobs/<int:id>', api.Jobdetailcbv.as_view(), name='job_list_cbv'),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
