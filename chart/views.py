from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import mixins, viewsets
from datetime import datetime

from .serializers import OhlcSerialiser
from .models import CandleStick

class ChartsListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CandleStick.objects.all()
    serializer_class = OhlcSerialiser
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')
        filters = {}

        if start:
            filters['timestamp__gte'] = datetime.fromtimestamp(int(self.request.GET['start']))
        if end:
            filters['timestamp__lte'] =  datetime.fromtimestamp(int(self.request.GET['end']))
        queryset = CandleStick.objects.filter(ticker=self.kwargs.get('ticker'), **filters).all()
        
        return queryset

