from django.contrib import admin
from user_profile_api.models import UserProfile, Room, Subject, Device
from django.utils import timezone
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from django.core.files.base import ContentFile
import os
from django import forms
from user_profile_api.services import get_default_user_device_id

class DeviceInline(admin.StackedInline):
    model = Device.users.through
    extra = 1



@admin.register(UserProfile)
class ManageUser(admin.ModelAdmin):
    list_display=('user_device_id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'profile_type', 'dni', 'address', 'phone', 'emergency_phone', 'fileImage')
    ordering=('user_device_id',)
    search_fields= ('user_device_id', 'dni', 'email', 'first_name', 'last_name')
    list_per_page=50
    readonly_fields=('date_created', 'last_updated')
    inlines = [DeviceInline]

    def save_model(self, request, obj, form, change):
        obj.last_updated = timezone.now()
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        default_user_device_id = get_default_user_device_id()
        form.base_fields['user_device_id'].initial = default_user_device_id
        return form


@admin.register(Room)
class ManageRoom(admin.ModelAdmin):
    list_display=('room','location')
    ordering=('id',)
    search_fields= ('id',)
    list_per_page=10


@admin.register(Subject)
class ManageSubject(admin.ModelAdmin):
    list_display=('subject','room','career', 'begin_hour', 'end_hour')
    ordering=('id',)
    search_fields= ('id','subject','room')
    list_per_page=10
    
    
@admin.register(Device)
class ManageDevice(admin.ModelAdmin):
    list_display=('id', 'device','date_purchased','is_active', 'is_synchronized')
    ordering=('id',)
    search_fields= ('id','device','date_purchased','user')
    list_per_page=10
  
