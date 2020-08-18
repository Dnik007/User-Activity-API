from rest_framework import serializers
from user_activity.models import User, UserActivity

class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserActivity
        fields =('start_time','end_time')

class UserSerializer(serializers.ModelSerializer):
    activity_periods = UserActivitySerializer(many=True)
    class Meta:
        model = User

        fields = ('id','real_name','tz','activity_periods')

    def create(self, validated_data):
        activity_data = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        for activity_data in activity_data:
            UserActivity.objects.create(user=user, **activity_data)
        return user
    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()

        return instance
