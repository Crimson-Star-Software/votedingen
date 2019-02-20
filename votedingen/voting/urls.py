from django.urls import path
from . import views

urlpatterns = [
    path('api/elections/', views.ElectionCreate.as_view()),
    path('api/candidates/', views.CandidateCreate.as_view()),
]