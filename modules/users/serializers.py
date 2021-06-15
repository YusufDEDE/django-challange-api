from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        profile = Profile(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            about_us=validated_data['about_us'],
        )
        profile.save()

        return profile

    class Meta:
        model = Profile
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'phone', 'about_us')
