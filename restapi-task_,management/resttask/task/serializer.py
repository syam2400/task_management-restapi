from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']


class TaskSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date', 'completed','image']
