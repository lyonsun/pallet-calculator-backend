from rest_framework import viewsets
from .models import Pallet
from .serializers import PalletSerializer

class PalletViewSet(viewsets.ModelViewSet):
    queryset = Pallet.objects.all().order_by('-updated_at')
    serializer_class = PalletSerializer