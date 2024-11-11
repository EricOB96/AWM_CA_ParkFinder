
from rest_framework import viewsets
from .models import Park
from .serializers import ParkSerializer

from django.views.generic import TemplateView

class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class MapView(TemplateView):
    template_name = 'map.html'
