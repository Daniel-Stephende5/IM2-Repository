from django.db import models
 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} on {self.post.title}'

# Removed SignUp model as it's not necessary when using User model
# class SignUp(models.Model):
#     uname = models.CharField(max_length=20)
#     upass = models.CharField(max_length=20)
#     
#     class Meta:
#         db_table="signup"
