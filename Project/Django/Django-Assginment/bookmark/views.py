from django.shortcuts import render
from django.http import HttpResponse, Http404
from bookmark.models import Bookmark


# Create your views here.
def bookmark_list(request):
    bookmarks = Bookmark.object.all()  # SELECT * FROM bookmark
    context = {"bookmarks": bookmarks}
    return render(request, "bookmark_list.html", context)


def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        raise Http404

    context = {"bookmark": bookmark}
    return render(request, "bookmark_detail.html", context)
