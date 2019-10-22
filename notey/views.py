from django.shortcuts import render
from notey.data import NOTEY

# Create your views here.

def notes_list(request):
  return render(request, "notey/notelist.html", {"notes": NOTEY})


# def notelist(request, id):
#   return render(request, "notey/notelist.html")
