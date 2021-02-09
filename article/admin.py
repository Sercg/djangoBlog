from django.contrib import admin

from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)
@admin.register(Article) #Decorators can be used with both functions and classes
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] # To make these attributes seen on admin panel
    list_display_links = ["title","created_date"] # Creates link between the article and the attributes seen on admin panel
    search_fields = ["title","content"]
    list_filter = ["created_date"]
    class Meta:
        model= Article

"""@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article","comment_author","comment_content","comment_date"] # To make these attributes seen on admin panel
    list_display_links = ["article","comment_content"] # Creates link between the article and the attributes seen on admin panel
    search_fields = ["comment_author","comment_content"]
    list_filter = ["created_date"]
    class Meta:
        model= Article
"""