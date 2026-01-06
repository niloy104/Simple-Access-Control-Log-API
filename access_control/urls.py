from django.urls import path
from .views import AccessLogListCreate, AccessLogRetrieveUpdateDelete

urlpatterns = [
    path('logs/', AccessLogListCreate.as_view(), name='log-list-create'),
    path('logs/<int:pk>/', AccessLogRetrieveUpdateDelete.as_view(), name='log-detail'),
]
