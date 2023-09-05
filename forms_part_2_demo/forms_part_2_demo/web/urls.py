from django.urls import path

from forms_part_2_demo.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
