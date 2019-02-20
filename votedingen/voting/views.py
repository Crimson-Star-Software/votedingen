from .models import Candidate, Election
from .serializers import CandidateSerializer, ElectionSerializer
from rest_framework import generics

class ElectionCreate(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class CandidateCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
