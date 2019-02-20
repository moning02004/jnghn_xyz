from django.contrib import admin

from .models import Archive, Attachment, CommentArchive


admin.site.register(Archive)
admin.site.register(Attachment)
admin.site.register(CommentArchive)