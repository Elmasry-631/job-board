from django.contrib.auth.urls import urlpatterns
from django.urls import path,include
from . import views


urlpatterns =[

    path('',views.job_list),
    path('<int:id>',views.job_detail),

]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
