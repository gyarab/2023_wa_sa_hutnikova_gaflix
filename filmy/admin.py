from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "footage", "director", "genres_display", "main_picture"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name", "director_name"]
    list_filter = ["year", "genres"]
    list_editable = ["year", "footage", "main_picture"]

class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year", "description"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
    list_editable = ["description"]

class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year", "description"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
    list_editable = ["description"]

class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
    list_filter = ["name"]


admin.site.register(Movie, MovieAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)
