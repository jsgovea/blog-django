from django.contrib import admin
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')
    fieldsets = ('Profile', {
        'fields': ('user', 'picture')
    }),
