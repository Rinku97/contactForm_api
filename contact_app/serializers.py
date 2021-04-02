from rest_framework import serializers


class ContactForm(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    phone = serializers.IntegerField()
    message = serializers.CharField(max_length=500)
