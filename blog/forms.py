from django import forms 
from .models import Post, Like,  Comment


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content', 'image', 'category', 'status')

class PostComment(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('content',)

class LikePost(forms.ModelForm):
    class Meta:
        model= Like
        fields = ()