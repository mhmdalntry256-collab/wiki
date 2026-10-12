from django.shortcuts import render
from django.http import Http404

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
