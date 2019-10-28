from django.db import models

class NotesList(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


# class NotesListItem(models.Model):

#   body = models.CharField(max_length=255)
#   notes = models.ForeignKey(to=NotesList, on_delete=models.CASCADE, related_name='items')

#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

#   def __str__(self):
#     return self.body
