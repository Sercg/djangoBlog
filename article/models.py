from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE) # usingon-delete parameter makes auto-deletion of articles that user created when user is deleted
    title = models.CharField(max_length = 50)
    content = RichTextField(verbose_name= "Article Content") # If we use verbose_name parameter, in admin panel, we see the title as given text
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    article_image = models.FileField(blank = True, null = True, verbose_name="Add an image")
    def __str__(self): #To make article title seen on admin panel
        return(self.title)
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name ="Article",related_name="comments")
    comment_author = models.CharField(max_length=30,verbose_name="author")
    comment_content = models.CharField(max_length=300,verbose_name="content")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return(self.comment_content)
    class Meta:
        ordering = ['-comment_date']
