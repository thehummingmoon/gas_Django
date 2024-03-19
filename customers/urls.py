from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('submit_request/', views.SubmitRequestView.as_view(), name='submit_request'),
    path('track_requests/', views.TrackRequestsView.as_view(), name='track_requests'),
    path('account_info/', views.AccountInfoView.as_view(), name='account_info'),
    # Add more URL patterns as needed
]