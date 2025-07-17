from django.contrib import admin

from .models import User, WorkerSchedule, AdditionalMaterials
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "sex",
        "role",
        "phone",
        "photo",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "registration_date",
    )
    list_display_links = (
        "id",
        "first_name",
        "username",
    )

    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "registration_date",
    )
    raw_id_fields = ("groups", "user_permissions")
    save_on_top = True


@admin.register(AdditionalMaterials)
class AdditionalMaterialsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "note",
        "image_tag",
    )

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


@admin.register(WorkerSchedule)
class WorkerScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "worker",
        "day_of_week",
        "start_time",
        "end_time",
        "appointment_duration",
    )
    list_filter = ("worker",)
