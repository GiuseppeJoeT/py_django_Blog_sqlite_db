from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


'''
Django allows us to append strings to table fields that act as boolean operators.
In our case, we are appending "__tle", which stands for "less-than-or-equal-to" (<=)
to our "published_date" field.
'''


# Function that handles the most 5 popular post VIEW in the home page
# def most_popular_post_list(request):

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "blogdetail.html", {'post': post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)  # pk???
        else:
            form = PostForm()  # ??? Function did't recognize
        return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            # check if details are valid
            post = form.save(commit=False)
            post.author = request.user
            # redirect the user to the page that will show
            # the submitted details
            post.published_date = timezone.now()
            post.save()  # save data to DB
            return redirect(post_detail, post.pk)
        else:
            # if the method is GET we instantiate the
            # BlogPostForm class giving it the post
            # we are editing and direct the user to it
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form})
