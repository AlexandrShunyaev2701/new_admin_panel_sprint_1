from django.contrib import admin
from .models import Genre, Filmwork, GanreFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class GenreFilmworkInline(admin.TabularInline):
    model = GanreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)

    list_display = ('id', 'title', 'type', 'creation_date', 'rating',)

    list_filter = ('type', 'creation_date',)

    search_fields = ('title', 'description', 'id')
