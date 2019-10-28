from django.shortcuts import render, redirect, get_object_or_404
from notey.data import NOTEY
from notey.models import NotesList
from notey.forms import NotesForm


def notes_list(request):
  notes = NotesList.objects.all()
  return render(request, "notey/notelist.html", {"notes": notes})

def note_detail(request, pk):
  note = NotesList.objects.get(pk=pk)
  return render(request, "notey/note_detail.html", {"note": note})

def notes_create(request):
  if request.method == "POST":
    form = NotesForm(request.POST)
    if form.is_valid():
      notes_list = form.save()
      return redirect(to=notes_list)
  else:
    form = NotesForm()

  return render(request, "notey/notes_create.html", {"form": form})

def notes_edit(request, pk):
  note = get_object_or_404(NotesList, pk=pk)

  if request.method == "POST":
    form = NotesForm(instance=note, data=request.POST)
    if form.is_valid():
      notes_list = form.save()
      return redirect(to='note_detail', pk=note.pk)
  else:
    form = NotesForm(instance=note)

  return render(request, 'notey/notes_edit.html', {
    "note": note,
    "form": form,
  })

def notes_delete(request, pk):
  note = get_object_or_404(NotesList, pk=pk)
  if request.method == 'POST':
    note.delete()
    return redirect(to='notes_list')

  return render(request, 'notey/note_delete.html', {"note": note})
