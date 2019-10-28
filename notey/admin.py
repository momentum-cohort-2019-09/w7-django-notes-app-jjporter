from django.contrib import admin

from notey.models import NotesList


class NotesListAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'created_at',
    'updated_at',
  )

admin.site.register(NotesList, NotesListAdmin)