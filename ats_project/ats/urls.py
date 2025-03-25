from django.urls import path
from .views import (
    CandidateCreateAPIView,
    CandidateUpdateAPIView,
    CandidateDeleteAPIView,
    CandidateSearchAPIView
)

urlpatterns = [
    path('candidates/create/', CandidateCreateAPIView.as_view(), name='create-candidate'),
    path('candidates/update/<int:pk>/', CandidateUpdateAPIView.as_view(), name='update-candidate'),
    path('candidates/delete/<int:pk>/', CandidateDeleteAPIView.as_view(), name='delete-candidate'),
    path('candidates/search/', CandidateSearchAPIView.as_view(), name='search-candidate'),
]
