from django.shortcuts import render
from notey.data import NOTEY

# Create your views here.

def notes_list(request):
  return render(request, "notey/notelist.html", {"notes": NOTEY})

def note_detail(request, id):
  return render(request, "notey/note_detail.html", {"note": NOTEY[id]})

