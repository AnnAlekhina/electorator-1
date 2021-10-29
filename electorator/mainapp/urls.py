from django.urls import path, include
from .api import (
    CandidateViewSet,
    ProtocolFirst,
    ProtocolSecondCreate, ProtocolsFirstList,
    ProtocolsFirstListQuantity, PercVotersViewSet,
    PresenceViewSet
)

urlpatterns = [
    path('protocols/first/', ProtocolFirst.as_view()),
    path('protocols/first/<int:prot_id>', ProtocolFirst.as_view()),
    path('protocols/second/', ProtocolSecondCreate.as_view()),
    path('uiks/<int:uik_id>/candidates/short/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
    path('uiks/<int:uik_id>/protocols/first/list/', ProtocolsFirstList.as_view()),
    path('uiks/<int:uik_id>/protocols/first/quantity/', ProtocolsFirstListQuantity.as_view()),
    path('presence/',PresenceViewSet.as_view()),
    path('votes/',PercVotersViewSet.as_view())
]
