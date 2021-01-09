from django.contrib import admin

# Register your models here.
from .models import Post, PostPoint,Comment

#admin.site.register(Post) #TODO УДАЛИТь
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

admin.site.register(PostPoint)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email',
                    'post','created',
                    'active')
    list_filter = ('active','created',
                   'updated')
    search_fields = ('name','email','body')
