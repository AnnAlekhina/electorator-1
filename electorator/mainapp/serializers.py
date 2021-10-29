from rest_framework import serializers

from accounts.models import Role
from .models import Candidate, Protocol1, Protocol2, Uik


class ProtocolFirstSerializer(serializers.ModelSerializer):
    """Creation the first protocol"""

    class Meta:
        model = Protocol1
        fields = ['id', 'num_uik', 'num_protocol_1', 'status', 'sum_bul', 'bad_form']


class ProtocolSecondSerializer(serializers.ModelSerializer):
    """Creation of the second protocol"""

    class Meta:
        model = Protocol2
        fields = ['num_uik', 'name', 'candidate_votes']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "info", "sum_votes"]


class CandidatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "info", "sum_votes"]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["role_user"]


class UikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ["num_uik"]


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ['num_tik', 'presence']


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name','party','sum_votes']

class TopTikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ['num_tik', 'population']

