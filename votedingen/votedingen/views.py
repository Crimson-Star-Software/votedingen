from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomeView(TemplateView):
    template_name = "index.html"
