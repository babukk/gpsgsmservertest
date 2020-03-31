
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Создаём класс для админки:
class CustomUserAdmin(UserAdmin):

    # Указываем django использовать формы (из forms.py):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)

# регистрируем класс в админке:
admin.site.register(CustomUser, CustomUserAdmin)
