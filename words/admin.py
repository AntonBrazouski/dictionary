from django.contrib import admin

from .models import Token


# Register your models here.
# class MeaningInline(admin.StackedInline):
#     model = Meaning
#     extra = 1

class TokenAdmin(admin.ModelAdmin):
    fields = ['word', 'type']
    # inlines = [MeaningInline]

admin.site.register([Token,])
