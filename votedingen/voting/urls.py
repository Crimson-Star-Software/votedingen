from django.urls import path
from . import views

urlpatterns = [
    path('api/elections/', views.ElectionCreate.as_view()),
    path('api/elections/<int:pk>', views.ElectionRead.as_view()),
    path('api/elections/<int:pk>/update', views.ElectionUpdate.as_view()),
    path('api/elections/<int:pk>/delete', views.ElectionDelete.as_view()),
    path('api/candidates/', views.CandidateCreate.as_view()),
    path('api/candidates/<int:pk>', views.CandidateRead.as_view()),
    path('api/candidates/<int:pk>/update', views.CandidateUpdate.as_view()),
    path('api/candidates/<int:pk>/delete', views.CandidateDelete.as_view()),
]