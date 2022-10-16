from django.contrib import admin

from blog.models import Post, Comment, Category



class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body']
    list_display = ['title', 'created_at', 'last_modified']
    search_fields = ['title', 'body']
    list_filter = ['title', 'created_at']


admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

