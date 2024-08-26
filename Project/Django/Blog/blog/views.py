from django.shortcuts import get_object_or_404, render
from blog.models import Blog

# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()

    visits = int(request.COOKIES.get("visits", 0)) + 1

    request.session["count"] = request.session.get("count", 0) + 1  # 추가

    context = {"blogs": blogs}

    response = render(request, "blog_list.html", context)
    response.set_cookie("visits", visits)  # visits라는 이름으로 visits값을 담아준다.
    return response


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
