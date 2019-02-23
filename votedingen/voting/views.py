from .models import Candidate, Election
from .serializers import CandidateSerializer, ElectionSerializer
from rest_framework import generics

class ElectionCreate(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionRead(generics.RetrieveAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionUpdate(generics.UpdateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionDelete(generics.DestroyAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class CandidateCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateRead(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateUpdate(generics.UpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDelete(generics.DestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
