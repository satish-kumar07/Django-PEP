from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note




def home(req):
    notes = Note.objects.all()
    return render(req, "index.html", context={'notes':notes})


def about(req):
    return render(req,"about.html")


def aboutView(req):
    return render(req, "about.html")


def saveDataView(req):
    print(req.POST)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/")
    
    note = Note(title = title, description= description)
    note.save()
    messages.success(req, "Detail saved")
    return redirect("/")


def indexView(req):
    notes = Note.objects.all()
    return render(req, "index.html", context={'notes':notes})

def deleteView(req,id):
     note=Note.objects.get(id=id)
     note.delete()
     messages.success(req,"Note deleted successfully")
     return redirect("/")
def editView(req,id):
    note=Note.objects.get(id=id)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/")
    
    note = Note(title = title, description= description)
    note.save()
    messages.success(req, "Detail updated")
    return redirect("/")

def updateViewpage(req, id):
    note = Note.objects.get(id=id)
    return render(req, "edit-page.html", {"note": note})

def updateDataView(req, id):

    note = Note.objects.get(id=id)

    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
        messages.error(req, "Fill all details")
        return redirect(f"/update-note/{id}")

    note.title = title
    note.description = description
    note.save()

    messages.success(req, "Note Updated Successfully")
    return redirect("/")