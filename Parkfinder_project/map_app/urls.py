from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet, MapView

# Register the API routes
router = DefaultRouter()
router.register(r'parks', ParkViewSet)

# Include the map view in urlpatterns
urlpatterns = [
    path('map/', MapView.as_view(), name='map'),  # Map view route
]

# Add router-generated API routes to urlpatterns
urlpatterns += router.urls
