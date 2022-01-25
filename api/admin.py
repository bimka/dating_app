from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import Client
from .form import ClientCreateForm, ClientChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = ClientCreateForm
    form = ClientChangeForm
    model = Client
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'get_avatar', 
            'gender')
    list_filter = ('email', 'is_staff', 'is_active', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'first_name', 'last_name', 
            'avatar', 'gender')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 
            'avatar', 'gender','is_staff', 'is_active',              
            'email', 'password1', 'password2',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_avatar(self, obj):
        print(repr(obj.avatar))
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" alt="" height="100px">')
        else:
            return mark_safe(f'<img src="" alt="">')

admin.site.register(Client, CustomUserAdmin)
