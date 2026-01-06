from django.shortcuts import render
from rest_framework import generics
from .models import AccessLog
from .serializers import AccessLogSerializer

class AccessLogListCreate(generics.ListCreateAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        card_id = self.request.GET.get('card_id')
        if card_id:
            queryset = queryset.filter(card_id=card_id)
        return queryset

class AccessLogRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
