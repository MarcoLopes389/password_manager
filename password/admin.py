from django.contrib.admin import register, ModelAdmin
from django.db import models
from .models import User

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('wordpass','email', 'phone','name','nick')
    search_fields = ('name', 'nick')