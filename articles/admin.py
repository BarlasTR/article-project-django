from django.contrib import admin
from .models import Article, Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "comment_author","comment_content", "comment_date"]
    class Meta:
        model = Comment



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author","created_date", "content"]
    list_display_links=["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article


