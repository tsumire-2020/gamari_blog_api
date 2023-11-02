from django.contrib import admin

from blog.models import Post

# Register your models here.

# Admin機能をここで付与してDBを触ったりするようにする機能
# admin site registar(Blog)

admin.site.register(Post)