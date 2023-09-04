from django.urls import path

from django_forms.web.views import index

urlpatterns = (
    path('',index,name='index'),

)