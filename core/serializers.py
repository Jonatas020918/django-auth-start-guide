from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'date_of_birth', 'address', 'phone_number', 'user_type']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data.get('date_of_birth'),
            address=validated_data.get('address'),
            phone_number=validated_data.get('phone_number'),
            user_type=validated_data.get('user_type', 'regular')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
