from django.urls import path
from . import views


urlpatterns = [
    path('', views.text_analysis, name='analyze'), # default url to view the text field form in frontend view
    path('analysis/<str:pk>/', views.result, name='analysis'), # url to show sentiment analysis result of the input text in frontend view
    path('api/analyze/', views.postAnalyze), # REST API endpoint to analyze text data and see the sentiment prediction in JSON data in REST API view 
]