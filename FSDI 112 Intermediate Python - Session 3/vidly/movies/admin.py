from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # tuple


class MovieAdmin(admin.ModelAdmin):
    # exclude = ('price', )
    # List what properties the user will capture
    # fields = ('title', 'stock')
    list_display = ('id', 'title', 'stock', 'price')  # props on the list table


    # Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
