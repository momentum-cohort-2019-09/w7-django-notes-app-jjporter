from django.shortcuts import render
from notey.data import NOTEY

# Create your views here.

def notes_list(request):
  return render(request, "notey/notes_list.html", {"notes": NOTEY})


