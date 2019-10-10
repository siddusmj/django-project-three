from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^signup$',views.signup),
    url(r'^ins$',views.ins),
    url(r'^index$',views.readData),
    url(r'^index$',views.displayData),
    url(r'^index$',views.getData),
    url(r'^updatedata$',views.updateData),
    url(r'^deletedata$',views.deleteData)
]