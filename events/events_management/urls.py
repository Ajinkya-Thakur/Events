from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.events, name='events'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<uuid:event_id>/', views.event_details, name='event_details'),
    path('delete-event/<uuid:event_id>/', views.delete_event, name='delete_event'),
    path('delete-transaction/<uuid:transaction_id>/', views.delete_transaction, name='delete_transaction')
]