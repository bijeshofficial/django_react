from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from django.core.exceptions import PermissionDenied

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    # queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied()
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
