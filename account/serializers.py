from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from account.models import MyUser
from .utils import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, label='Password')

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегестрирован.')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                message = 'Unable to log in with provided credentials'
                raise serializers.ValidationError(message, code='authorization')

        else:
            message = "Must include 'email' and 'password'"
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs

# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, min_length=6)
#     password2 = serializers.CharField(required=True, min_length=6)
#
#     def validate_old_password(self, old_pass):
#         user = self.context.get('request').user
#         if not user.check_password(old_pass):  # check_password - built-in function
#             raise serializers.ValidationError('Неверный пароль!')
#         return old_pass
#
#     def validate(self, attrs):
#         pass1 = attrs.get('password')
#         pass2 = attrs.get('password2')
#
#         if pass1 != pass2:
#             raise serializers.ValidationError('Пароли не совпадают')
#         return attrs
#
#     def set_user_password(self):
#         user = self.context.get('request').user
#         password = self.validated_data.get('password')
#         user.set_password(password)
#         user.save()
