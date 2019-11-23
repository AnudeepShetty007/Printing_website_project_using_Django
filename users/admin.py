from django.contrib import admin
from .models import contactus,Banners

from .models import Post
admin.site.register(Post)


admin.site.register(contactus)
admin.site.register(Banners)
