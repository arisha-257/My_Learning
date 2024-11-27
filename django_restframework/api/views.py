from rest_framework import generics 
from .models import Item,Location
from .serializers import ItemSerializer,LocationSerializer

class ItemList(generics.ListCreateAPIView):
    
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = Item.objects.all()
        Location_id=self.request.query_params.get('Location',None)
        if Location_id is not None:
            queryset=queryset.filter(itemLocation=Location_id)
        return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer   