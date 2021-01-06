from django.contrib import admin

from .models import Meaning, Token


# Register your models here.
admin.site.register([Token, Meaning])
