from django.contrib import admin
from .models import Task,Invitation
from django.utils.html import format_html
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.utils.html import format_html

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'used', 'created_at', 'send_invitation_button')

    def get_urls(self):
        """
        Add custom URLs to the admin interface.
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                'invitation/<int:pk>/send/',
                self.admin_site.admin_view(self.send_invitation_view),
                name='send_invitation',
            ),
        ]
        return custom_urls + urls

    def send_invitation_view(self, request, pk, *args, **kwargs):
        """
        Custom view to send an invitation.
        """
        invitation = Invitation.objects.get(pk=pk)
        if invitation.used:
            self.message_user(request, "Invitation already used.", level=messages.WARNING)
        else:
            current_site = get_current_site(request)
            invitation_link = f"http://{current_site.domain}/register/{invitation.token}/"

            send_mail(
                subject="Invitation to Join",
                message=f"Register here: {invitation_link}",
                from_email="admin@example.com",
                recipient_list=[invitation.email],
            )
            self.message_user(request, f"Invitation sent to {invitation.email}.", level=messages.SUCCESS)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def send_invitation_button(self, obj):
        """
        Add a button in the admin panel to send an individual invitation.
        """
        if obj.used:
            return format_html('<span style="color: gray;">Used</span>')
        return format_html(
            '<a class="button" href="{}">Send Invitation</a>',
            reverse('admin:send_invitation', args=[obj.pk]),
        )
    send_invitation_button.short_description = "Actions"

admin.site.register(Invitation, InvitationAdmin)

# Register your models here.
admin.site.register(Task)
