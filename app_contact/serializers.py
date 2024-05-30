from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.serializers import ModelSerializer

from .models import ContactModel, InfoForMainPage


class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'

    def create(self, validated_data):
        contact = ContactModel.objects.create(**validated_data)
        self.send_contact_email(contact)
        return contact

    def send_contact_email(self, contact):
        info = InfoForMainPage.objects.first()
        if info and info.email:
            subject = 'New Contact Message'
            message = f"Message from {contact.user_first_name} ({contact.user_email}):\n\n{contact.user_message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [info.email]
            send_mail(subject, message, from_email, recipient_list)


class InformationForMainPageSerializer(ModelSerializer):
    class Meta:
        model = InfoForMainPage
        fields = '__all__'
