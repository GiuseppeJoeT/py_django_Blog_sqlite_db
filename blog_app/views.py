from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogtests.html", {'posts': posts})


'''
Django allows us to append strings to table fields that act as boolean operators.
In our case, we are appending "__tle", which stands for "less-than-or-equal-to" (<=)
to our "published_date" field.
'''
