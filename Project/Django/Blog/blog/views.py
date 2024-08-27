from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from blog.forms import BlogForm
from blog.models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")

    visits = int(request.COOKIES.get("visits", 0)) + 1

    request.session["count"] = request.session.get("count", 0) + 1  # 추가

    context = {"blogs": blogs}

    response = render(request, "blog_list.html", context)
    response.set_cookie("visits", visits)  # visits라는 이름으로 visits값을 담아준다.
    return response


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {"blog": blog}
    return render(request, "blog_detail.html", context)


@login_required()
def blog_create(request):
    # if not request.user.is_authenticated:
    #   return redirect(reverse('login'))
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)  # 블로그 모델만 생성
        blog.author = request.user  # author는 현재 로그인 된 유저
        blog.save()
        # kwargs는 reverse 함수에서 URL을 생성할 때, URL 패턴에서 요구하는 동적 경로 매개변수에 값을 전달하기 위해 사용
        return redirect(reverse("blog_detail", kwargs={"pk": blog.pk}))

    context = {"form": form}
    return render(request, "blog_create.html", context)


@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)

    form = BlogForm(request.POST or None, instance=blog)  # instance로 기초데이터 세팅
    if form.is_valid():
        blog = form.save()
        return redirect(reverse("blog_detail", kwargs={"pk": blog.pk}))

    context = {
        "blog": blog,
        "form": form,
    }

    return render(request, "blog_update.html", context)
