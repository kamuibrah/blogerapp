from django.contrib import admin

from .models import Author, Article

class AuthorAdmin(admin.ModelAdmin):
    list_display=("name", "contact", "email")


admin.site.register(Author,AuthorAdmin)


