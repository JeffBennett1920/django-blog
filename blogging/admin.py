from django.contrib import admin
from blogging.models import Post, Category


class CategoryPostInline(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryPostInline,
    ]
    model = Post


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
