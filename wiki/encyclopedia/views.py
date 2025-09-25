from django.shortcuts import render
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    desired_page = util.get_entry(title)
    if desired_page is None:
        return render(request, "encyclopedia/nopage.html", {
            "title": title
        })
    else:
        html_desired_page = markdown.markdown(desired_page)
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": html_desired_page
        })


