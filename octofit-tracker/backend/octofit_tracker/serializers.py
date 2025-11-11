from rest_framework import serializers
from .models import Team, User, Activity, Workout, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Leaderboard
        fields = '__all__'
