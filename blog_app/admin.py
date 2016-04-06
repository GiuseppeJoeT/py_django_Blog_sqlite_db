from django.contrib import admin
from .models import Post

admin.site.register(Post)

# With the line above we are registering the Post model.
# placed in models.py
