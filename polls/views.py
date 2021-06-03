from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from polls.serializers import PollListItemSerializer, PollSerializer
from polls.models import Poll


class PollsListView(ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollListItemSerializer


class PollsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
