from django.shortcuts import render
from django.http import Http404
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Page not found")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })


def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new.html", {
                "error": "An encyclopedia entry with this title already exists."
            })
        
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })
        
    return render(request, "encyclopedia/new.html")


def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    
    content = util.get_entry(title)
    if content is None:
        raise Http404("Page not found")
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return entry(request, random_entry)
