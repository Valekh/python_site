from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)


