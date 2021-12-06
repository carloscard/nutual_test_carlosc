from django.urls import path
from avm_api import views


urlpatterns = [
    path('avm-api/', views.AvmApiView.as_view()),

]
