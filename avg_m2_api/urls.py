from django.urls import path
from avg_m2_api import views


urlpatterns = [
    path('avg-m2-api/', views.AvgM2Api.as_view()),

]
