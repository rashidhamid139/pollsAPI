from rest_framework import serializers
from .models import Friend, Belonging, Borrowed


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name')


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = ("id", "name")

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ("id", "what", "who", "when", "returned")