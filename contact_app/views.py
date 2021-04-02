from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .serializers import ContactForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ContactFormApi(APIView):

    def post(self, request, format=None):
        serializer = ContactForm(data=request.data)

        if serializer.is_valid():
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            phone = serializer.data['phone']
            email = serializer.data['email']
            message = serializer.data['message']
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'message': message
            }
            template = render_to_string('pages/email_template.html', context)
            email = EmailMessage(
                'Inquiry on your website from ' + first_name + '  ' + last_name,
                template,
                settings.EMAIL_HOST_USER,
                ['rinkurb0@gmail.com', 'vikrantgautam947@gmail.com', 'tyagi11n@gmail.com'],
            )
            email.fail_silently = False
            email.send()
            messages.success(request,
                             ': Your enquiry has been made successfully')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

